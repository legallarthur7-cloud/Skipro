import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://ktpbhznjzndhbxwoklvq.supabase.co';
const supabaseKey = 'sb_publishable_NM3F43nPoj0Bkx6_K5l6dA_rKrnYq2E';

export const supabase = createClient(supabaseUrl, supabaseKey);

async function get(key, shared = false) {
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) throw new Error('Not authenticated');
  const { data, error } = await supabase
    .from('kv_store')
    .select('value')
    .eq('user_id', user.id)
    .eq('key', key)
    .eq('shared', shared)
    .single();
  if (error || !data) throw new Error(`Key not found: ${key}`);
  return { key, value: data.value, shared };
}

async function set(key, value, shared = false) {
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) throw new Error('Not authenticated');
  const { error } = await supabase
    .from('kv_store')
    .upsert({ user_id: user.id, key, value, shared, updated_at: new Date().toISOString() }, { onConflict: 'user_id,key,shared' });
  if (error) throw error;
  return { key, value, shared };
}

async function del(key, shared = false) {
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) throw new Error('Not authenticated');
  await supabase.from('kv_store').delete().eq('user_id', user.id).eq('key', key).eq('shared', shared);
  return { key, deleted: true, shared };
}

async function list(prefix = '', shared = false) {
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) throw new Error('Not authenticated');
  const { data, error } = await supabase
    .from('kv_store')
    .select('key')
    .eq('user_id', user.id)
    .eq('shared', shared)
    .like('key', `${prefix}%`);
  if (error) throw error;
  return { keys: (data || []).map(r => r.key), prefix, shared };
}

window.storage = { get, set, delete: del, list };
