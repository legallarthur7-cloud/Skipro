import Stripe from 'stripe';
import { createClient } from '@supabase/supabase-js';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

const supabaseAdmin = createClient(
  process.env.VITE_SUPABASE_URL || 'https://ktpbhznjzndhbxwoklvq.supabase.co',
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

const RES_KEY = 'skipro-reservations-v1';

export const config = { api: { bodyParser: false } };

function buffer(readable) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    readable.on('data', (chunk) => chunks.push(chunk));
    readable.on('end', () => resolve(Buffer.concat(chunks)));
    readable.on('error', reject);
  });
}

async function getUserIdForEmail(email) {
  const { data: usersData, error } = await supabaseAdmin.auth.admin.listUsers();
  if (error) { console.error(error); return null; }
  const user = usersData.users.find(u => u.email === email);
  return user ? user.id : null;
}

async function setAbonnementForEmail(email, actif) {
  if (!email) return;
  const userId = await getUserIdForEmail(email);
  if (!userId) { console.error('Utilisateur introuvable pour', email); return; }

  await supabaseAdmin.from('kv_store').upsert({
    user_id: userId,
    key: 'skipro-abonnement-v1',
    value: actif ? 'actif' : 'inactif',
    shared: false,
    updated_at: new Date().toISOString()
  }, { onConflict: 'user_id,key,shared' });
}

async function markGuardUsed(userId, guardKey) {
  if (!userId || !guardKey) return;
  await supabaseAdmin.from('kv_store').upsert({
    user_id: userId,
    key: guardKey,
    value: 'used',
    shared: true,
    updated_at: new Date().toISOString()
  }, { onConflict: 'user_id,key,shared' });
}

async function isGuardAlreadyUsed(guardKey) {
  const { data } = await supabaseAdmin
    .from('kv_store')
    .select('value')
    .eq('key', guardKey)
    .eq('shared', true)
    .limit(1);
  return !!(data && data.length > 0);
}

// Confirme d'un coup tous les cours d'une réservation multi-cours (même groupId) une fois
// l'acompte payé côté client. Voir create-deposit-session.js pour la création de la session
// et public-booking.js pour la structure des réservations (un enregistrement par cours, groupId partagé).
async function confirmReservationDeposit(session) {
  const { groupId, userId } = session.metadata || {};
  if (!userId || !groupId) {
    console.error('Webhook acompte réservation : groupId ou userId manquant dans les metadata', session.metadata);
    return;
  }

  const { data } = await supabaseAdmin
    .from('kv_store')
    .select('value')
    .eq('user_id', userId)
    .eq('key', RES_KEY)
    .eq('shared', false)
    .limit(1);
  const raw = data && data.length > 0 ? data[0].value : null;
  if (!raw) { console.error('Aucune réservation trouvée pour', userId); return; }

  const reservations = JSON.parse(raw);
  const updated = reservations.map(r =>
    String(r.groupId) === String(groupId)
      // "Acompte reçu" et non "Acompte payé" : seule cette valeur fait partie des statuts de
      // paiement reconnus par l'application (voir PAIEMENT_STATUTS dans App.jsx).
      ? { ...r, statut: 'Confirmée', paiement: 'Acompte reçu' }
      : r
  );

  await supabaseAdmin.from('kv_store').upsert({
    user_id: userId,
    key: RES_KEY,
    value: JSON.stringify(updated),
    shared: false,
    updated_at: new Date().toISOString()
  }, { onConflict: 'user_id,key,shared' });
}

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end();

  const buf = await buffer(req);
  const sig = req.headers['stripe-signature'];
  let event;

  try {
    event = stripe.webhooks.constructEvent(buf, sig, process.env.STRIPE_WEBHOOK_SECRET);
  } catch (err) {
    console.error('Signature webhook invalide', err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  try {
    switch (event.type) {
      case 'checkout.session.completed': {
        const session = event.data.object;

        // Acompte de réservation (multi-cours) : rien à voir avec l'abonnement SkiPro,
        // on traite ça séparément et on sort tout de suite.
        if (session.metadata?.type === 'reservation-deposit') {
          await confirmReservationDeposit(session);
          break;
        }

        const email = session.customer_email || session.customer_details?.email;
        await setAbonnementForEmail(email, true);

        const userId = await getUserIdForEmail(email);
        const telephone = session.metadata?.telephone || '';

        // Enregistre le telephone comme "essai utilise"
        if (userId && telephone) {
          await markGuardUsed(userId, `trial-guard:phone:${telephone}`);
        }

        // Verifie l'empreinte de la carte bancaire utilisee
        if (session.subscription) {
          try {
            const subscription = await stripe.subscriptions.retrieve(session.subscription, {
              expand: ['default_payment_method']
            });
            const fingerprint = subscription.default_payment_method?.card?.fingerprint;

            if (fingerprint) {
              const cardGuardKey = `trial-guard:card:${fingerprint}`;
              const cardAlreadyUsed = await isGuardAlreadyUsed(cardGuardKey);

              if (cardAlreadyUsed && subscription.status === 'trialing') {
                // Cette carte a deja beneficie d'un essai avec un autre compte : on coupe l'essai immediatement
                await stripe.subscriptions.update(session.subscription, { trial_end: 'now' });
                console.log('Essai coupe immediatement (carte deja utilisee) pour', email);
              }

              if (userId) await markGuardUsed(userId, cardGuardKey);
            }
          } catch (cardErr) {
            console.error('Erreur verification empreinte carte', cardErr);
          }
        }
        break;
      }
      case 'customer.subscription.deleted': {
        const sub = event.data.object;
        const customer = await stripe.customers.retrieve(sub.customer);
        await setAbonnementForEmail(customer.email, false);
        break;
      }
      case 'invoice.payment_failed': {
        const invoice = event.data.object;
        await setAbonnementForEmail(invoice.customer_email, false);
        break;
      }
    }
    res.status(200).json({ received: true });
  } catch (err) {
    console.error('Erreur traitement webhook', err);
    res.status(500).json({ error: err.message });
  }
}
