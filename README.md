# SkiPro

SaaS de gestion pour moniteurs de ski indépendants — Dashboard, Calendrier, Réservations,
Clients, Paiements & Factures, Statistiques, Paramètres, plus un formulaire public de
réservation multilingue.

## Démarrer en local

```bash
npm install
npm run dev
```

Ouvre http://localhost:5173 pour l'app moniteur, et http://localhost:5173/reserver pour
le formulaire public client.

## État actuel du projet

- Le stockage des données utilise un **pont temporaire vers localStorage**
  (`src/lib/storage-shim.js`), pour que tout fonctionne immédiatement, sans backend.
- L'authentification (`AuthScreen` dans `App.jsx`) est **un écran visuel uniquement** :
  cliquer sur "Se connecter" ou "Créer mon compte" fait juste entrer dans l'app, sans
  vérification réelle de mot de passe.
- **Chaque navigateur a ses propres données.** Deux personnes sur deux appareils ne
  partagent rien tant que Supabase n'est pas branché (voir ci-dessous).

C'est volontaire : ça permet de tester et de montrer le produit tout de suite, pendant
que tu prépares la vraie infrastructure.

## Passer à un vrai système multi-utilisateurs (Supabase)

1. Crée un compte sur [supabase.com](https://supabase.com) et un nouveau projet.
2. `npm install @supabase/supabase-js`
3. Active l'authentification par e-mail/mot de passe dans Supabase (Authentication → Providers).
4. Crée une table `kv_store` (voir le détail complet en commentaire dans
   `src/lib/storage-shim.js`) avec Row Level Security activée, pour que chaque moniteur
   ne voie que ses propres données.
5. Remplace le contenu de `src/lib/storage-shim.js` par de vrais appels Supabase
   (exemple de code fourni en commentaire dans ce même fichier).
6. Remplace la logique de `AuthScreen` (dans `App.jsx`) par de vrais appels
   `supabase.auth.signInWithPassword(...)` et `supabase.auth.signUp(...)`.

Aucun autre fichier n'a besoin d'être modifié : tout le reste de l'app (Dashboard,
Calendrier, Réservations, Clients, Paiements, Statistiques) continue de fonctionner
à l'identique, puisqu'il ne parle qu'à `window.storage`.

## Déployer sur Vercel

1. Pousse ce dossier sur un repo GitHub.
2. Va sur [vercel.com](https://vercel.com) → "Add New Project" → sélectionne le repo.
3. Vercel détecte Vite automatiquement (build command `npm run build`, output `dist`).
4. Une fois Supabase branché, ajoute tes variables d'environnement dans
   Vercel → Settings → Environment Variables :
   - `VITE_SUPABASE_URL`
   - `VITE_SUPABASE_ANON_KEY`
5. Déploie. Le fichier `vercel.json` fourni gère déjà le routage pour que
   `/reserver` fonctionne correctement (page publique de réservation).

## Nom de domaine

Achète un nom de domaine (OVH, Gandi, Namecheap...) et connecte-le à Vercel dans
Settings → Domains une fois le projet déployé.

## Structure du projet

```
src/
  main.jsx          → point d'entrée, routage simple (/ vs /reserver)
  App.jsx           → l'app moniteur complète (dashboard, calendrier, etc.)
  BookingPage.jsx    → le formulaire public multilingue pour les clients
  lib/
    storage-shim.js → pont de stockage (localStorage → à remplacer par Supabase)
```
