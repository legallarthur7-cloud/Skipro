import { createClient } from '@supabase/supabase-js';

const supabaseAdmin = createClient(
  process.env.VITE_SUPABASE_URL || 'https://ktpbhznjzndhbxwoklvq.supabase.co',
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

const SETTINGS_KEY = 'skipro-settings-v1';
const RES_KEY = 'skipro-reservations-v1';

function timeToMinutes(t) {
  const [h, m] = String(t).split(':').map(Number);
  return h * 60 + m;
}
function overlaps(aStart, aEnd, bStart, bEnd) {
  return aStart < bEnd && aEnd > bStart;
}

async function getUserIdForSlug(slug) {
  const cleanSlug = String(slug).toLowerCase().replace(/[^a-z0-9-]/g, '');
  const { data } = await supabaseAdmin
    .from('kv_store')
    .select('value')
    .eq('key', `slug-registry:${cleanSlug}`)
    .eq('shared', true)
    .limit(1);
  return data && data.length > 0 ? data[0].value : null;
}

async function getRow(userId, key) {
  const { data } = await supabaseAdmin
    .from('kv_store')
    .select('value')
    .eq('user_id', userId)
    .eq('key', key)
    .eq('shared', false)
    .limit(1);
  return data && data.length > 0 ? data[0].value : null;
}

export default async function handler(req, res) {
  try {
    if (req.method === 'GET') {
      const { slug } = req.query;
      if (!slug) return res.status(400).json({ error: 'slug requis' });

      const userId = await getUserIdForSlug(slug);
      if (!userId) return res.status(404).json({ error: 'Moniteur introuvable' });

      const settingsRaw = await getRow(userId, SETTINGS_KEY);
      const settings = settingsRaw ? JSON.parse(settingsRaw) : null;
      if (!settings) return res.status(404).json({ error: 'Profil introuvable' });

      const reservationsRaw = await getRow(userId, RES_KEY);
      const reservations = reservationsRaw ? JSON.parse(reservationsRaw) : [];

      // On ne renvoie que les creneaux occupes (pas les infos clients), pour l'affichage des disponibilites
      const busySlots = reservations
        .filter(r => r.statut !== 'Annulée')
        .map(r => ({ date: r.date, heureDebut: r.heureDebut, heureFin: r.heureFin }));

      const publicSettings = {
        nom: settings.nom,
        profession: settings.profession,
        devise: settings.devise,
        matinDebut: settings.matinDebut,
        matinFin: settings.matinFin,
        apresMidiDebut: settings.apresMidiDebut,
        apresMidiFin: settings.apresMidiFin,
        tarifSkiHaute: settings.tarifSkiHaute,
        tarifSkiBasse: settings.tarifSkiBasse,
        tarifSnowboardHaute: settings.tarifSnowboardHaute,
        tarifSnowboardBasse: settings.tarifSnowboardBasse,
        tarifDemiJourneeHaute: settings.tarifDemiJourneeHaute,
        tarifDemiJourneeBasse: settings.tarifDemiJourneeBasse,
        tarifJourneeHaute: settings.tarifJourneeHaute,
        tarifJourneeBasse: settings.tarifJourneeBasse,
        hauteSaisonDebut: settings.hauteSaisonDebut,
        hauteSaisonFin: settings.hauteSaisonFin,
        seasonMode: settings.seasonMode,
        zoneVacances: settings.zoneVacances,
        joursRepos: settings.joursRepos,
        langue: settings.langue
      };

      return res.status(200).json({ userId, settings: publicSettings, busySlots });
    }

    if (req.method === 'POST') {
      const { slug, cours } = req.body;
      if (!slug || !Array.isArray(cours) || cours.length === 0) {
        return res.status(400).json({ error: 'slug et cours (tableau) requis' });
      }
      for (const c of cours) {
        if (!c.date || !c.heureDebut || !c.heureFin) {
          return res.status(400).json({ error: 'date, heureDebut et heureFin requis pour chaque cours' });
        }
      }

      const userId = await getUserIdForSlug(slug);
      if (!userId) return res.status(404).json({ error: 'Moniteur introuvable' });

      const reservationsRaw = await getRow(userId, RES_KEY);
      const reservations = reservationsRaw ? JSON.parse(reservationsRaw) : [];

      // Vérification anti-conflit côté serveur : on refuse si un cours du lot chevauche
      // une réservation déjà enregistrée, OU un autre cours du même lot.
      for (let i = 0; i < cours.length; i++) {
        const c = cours[i];
        const newStart = timeToMinutes(c.heureDebut);
        const newEnd = timeToMinutes(c.heureFin);
        const conflictExisting = reservations.some(r =>
          r.date === c.date &&
          r.statut !== 'Annulée' &&
          overlaps(newStart, newEnd, timeToMinutes(r.heureDebut), timeToMinutes(r.heureFin))
        );
        const conflictSelf = cours.some((c2, j) =>
          j !== i && c2.date === c.date && overlaps(newStart, newEnd, timeToMinutes(c2.heureDebut), timeToMinutes(c2.heureFin))
        );
        if (conflictExisting || conflictSelf) {
          return res.status(409).json({ error: `Un des créneaux demandés (${c.date} ${c.heureDebut}-${c.heureFin}) vient d'être pris ou chevauche un autre cours de la même réservation. Merci de vérifier tes horaires.` });
        }
      }

      const groupId = Date.now();
      const newReservations = cours.map((c, idx) => ({
        ...c,
        id: groupId + idx,
        groupId,
        statut: 'En attente',
        paiement: 'Non payé',
        // Le client peut indiquer une préférence sur la page publique (voir BookingPage.jsx) ;
        // ça reste purement informatif, aucun paiement n'est traité ici.
        modePaiement: c.modePaiement || 'Non renseigné'
      }));

      reservations.push(...newReservations);

      await supabaseAdmin.from('kv_store').upsert({
        user_id: userId,
        key: RES_KEY,
        value: JSON.stringify(reservations),
        shared: false,
        updated_at: new Date().toISOString()
      }, { onConflict: 'user_id,key,shared' });

      return res.status(200).json({ ok: true, groupId, ids: newReservations.map(r => r.id) });
    }

    return res.status(405).json({ error: 'Method not allowed' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}
