/**
 * STORAGE SHIM
 * ------------
 * Le code de l'app (copié depuis le prototype Claude) appelle `window.storage.get/set/delete/list`.
 * Ce fichier fournit cette même API, mais branchée sur `localStorage` pour que l'app
 * fonctionne immédiatement en local et en démo, SANS backend.
 *
 * LIMITE IMPORTANTE : localStorage est propre à CE navigateur. Deux personnes sur deux
 * appareils différents ne partagent pas les mêmes données. Pour un vrai multi-utilisateur
 * (chaque moniteur ne voit que ses propres données), il faut remplacer le contenu des
 * fonctions ci-dessous par des appels à Supabase (voir le bloc "MIGRATION SUPABASE" en bas).
 */

const ns = (shared) => (shared ? 'skipro:shared:' : 'skipro:private:');

async function get(key, shared = false) {
  const raw = localStorage.getItem(ns(shared) + key);
  if (raw === null) throw new Error(`Key not found: ${key}`);
  return { key, value: raw, shared };
}

async function set(key, value, shared = false) {
  localStorage.setItem(ns(shared) + key, value);
  return { key, value, shared };
}

async function del(key, shared = false) {
  localStorage.removeItem(ns(shared) + key);
  return { key, deleted: true, shared };
}

async function list(prefix = '', shared = false) {
  const prefixFull = ns(shared) + prefix;
  const keys = Object.keys(localStorage)
    .filter((k) => k.startsWith(prefixFull))
    .map((k) => k.slice(ns(shared).length));
  return { keys, prefix, shared };
}

window.storage = { get, set, delete: del, list };

/**
 * ============================================================================
 * MIGRATION SUPABASE (à faire quand tu es prêt pour le vrai multi-utilisateur)
 * ============================================================================
 *
 * 1. Crée un projet sur https://supabase.com, récupère l'URL et la clé publique (anon key).
 * 2. `npm install @supabase/supabase-js`
 * 3. Crée une table `kv_store` avec les colonnes :
 *      user_id  uuid       (référence auth.users)
 *      key      text
 *      value    text
 *      shared   boolean
 *      updated_at timestamptz default now()
 *    + une contrainte unique sur (user_id, key, shared)
 *    + active la Row Level Security avec une policy du type :
 *      "user_id = auth.uid()" pour que chacun ne voie que ses propres lignes
 *      (et une policy à part, plus permissive, pour les lignes shared = true si besoin).
 *
 * 4. Remplace le contenu de ce fichier par quelque chose comme :
 *
 *    import { createClient } from '@supabase/supabase-js';
 *    const supabase = createClient(import.meta.env.VITE_SUPABASE_URL, import.meta.env.VITE_SUPABASE_ANON_KEY);
 *
 *    async function get(key, shared = false) {
 *      const { data: { user } } = await supabase.auth.getUser();
 *      const { data, error } = await supabase.from('kv_store').select('value')
 *        .eq('user_id', user.id).eq('key', key).eq('shared', shared).single();
 *      if (error || !data) throw new Error('Key not found: ' + key);
 *      return { key, value: data.value, shared };
 *    }
 *
 *    async function set(key, value, shared = false) {
 *      const { data: { user } } = await supabase.auth.getUser();
 *      await supabase.from('kv_store').upsert({ user_id: user.id, key, value, shared });
 *      return { key, value, shared };
 *    }
 *
 *    // ... etc pour delete/list, en suivant le même principe.
 *
 * Le reste du code de l'app (Dashboard, Calendrier, Réservations, etc.) n'a besoin
 * d'AUCUNE modification : il continue d'appeler window.storage.get/set comme avant.
 */
