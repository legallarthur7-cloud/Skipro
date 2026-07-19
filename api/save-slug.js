import { createClient } from '@supabase/supabase-js';

const supabaseAdmin = createClient(
  process.env.VITE_SUPABASE_URL || 'https://ktpbhznjzndhbxwoklvq.supabase.co',
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const { userId, slug } = req.body;
    if (!userId || !slug) return res.status(400).json({ error: 'userId et slug requis' });

    const cleanSlug = String(slug).toLowerCase().replace(/[^a-z0-9-]/g, '');
    if (cleanSlug.length < 3) return res.status(400).json({ error: 'Identifiant trop court (3 caracteres minimum)' });

    const registryKey = `slug-registry:${cleanSlug}`;

    const { data: existing } = await supabaseAdmin
      .from('kv_store')
      .select('user_id, value')
      .eq('key', registryKey)
      .eq('shared', true)
      .limit(1);

    if (existing && existing.length > 0 && existing[0].value !== userId) {
      return res.status(409).json({ error: 'Cet identifiant est deja pris' });
    }

    await supabaseAdmin.from('kv_store').upsert({
      user_id: userId,
      key: registryKey,
      value: userId,
      shared: true,
      updated_at: new Date().toISOString()
    }, { onConflict: 'user_id,key,shared' });

    res.status(200).json({ ok: true, slug: cleanSlug });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}
