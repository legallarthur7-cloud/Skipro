import Stripe from 'stripe';
import { createClient } from '@supabase/supabase-js';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

const supabaseAdmin = createClient(
  process.env.VITE_SUPABASE_URL || 'https://ktpbhznjzndhbxwoklvq.supabase.co',
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

export const config = { api: { bodyParser: false } };

function buffer(readable) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    readable.on('data', (chunk) => chunks.push(chunk));
    readable.on('end', () => resolve(Buffer.concat(chunks)));
    readable.on('error', reject);
  });
}

async function setAbonnementForEmail(email, actif) {
  if (!email) return;
  const { data: usersData, error: userError } = await supabaseAdmin.auth.admin.listUsers();
  if (userError) { console.error(userError); return; }
  const user = usersData.users.find(u => u.email === email);
  if (!user) { console.error('Utilisateur introuvable pour', email); return; }

  await supabaseAdmin.from('kv_store').upsert({
    user_id: user.id,
    key: 'skipro-abonnement-v1',
    value: actif ? 'actif' : 'inactif',
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
        await setAbonnementForEmail(session.customer_email || session.customer_details?.email, true);
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
