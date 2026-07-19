with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0
total = 2

old_handle = """  const handleSaveSettings = async (form) => { setSettings(form); await persistSettings(form); };"""

new_handle = """  const handleSaveSettings = async (form) => {
    if (form.slug) {
      try {
        const { data: { user } } = await supabase.auth.getUser();
        const res = await fetch('/api/save-slug', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ userId: user?.id, slug: form.slug }),
        });
        const data = await res.json();
        if (!res.ok) return { ok: false, error: data.error };
      } catch (e) {
        return { ok: false, error: 'Erreur de connexion.' };
      }
    }
    setSettings(form);
    await persistSettings(form);
    return { ok: true };
  };"""

if old_handle in content:
    content = content.replace(old_handle, new_handle, 1)
    changes += 1
    print("OK 1/2 - handleSaveSettings mis a jour avec verification du slug")
else:
    print("ERREUR 1/2 - handleSaveSettings non trouve")

old_button = """        <button onClick={() => { onSave(form); setSaved(true); setTimeout(() => setSaved(false), 2000); }} style={{ background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '10px 22px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}>{tUI('btnSave', langue)}</button>"""

new_button = """        <button onClick={async () => { const result = await onSave(form); if (result && result.ok === false) { alert(tUI('slugTaken', langue)); } else { setSaved(true); setTimeout(() => setSaved(false), 2000); } }} style={{ background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '10px 22px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}>{tUI('btnSave', langue)}</button>"""

if old_button in content:
    content = content.replace(old_button, new_button, 1)
    changes += 1
    print("OK 2/2 - Bouton Enregistrer gere la reponse (conflit de slug)")
else:
    print("ERREUR 2/2 - Bouton Enregistrer non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/{total} modifications appliquees.")
