with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0
total = 4

# 1. Ajouter DAYS_FULL_MAP juste apres DAYS_SHORT_MAP
old_anchor = """const DAYS_SHORT_MAP = {
  Français: ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'],
  Anglais: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  Espagnol: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'],
  Italien: ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'],
  Portugais: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
};"""

new_anchor = """const DAYS_SHORT_MAP = {
  Français: ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'],
  Anglais: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  Espagnol: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'],
  Italien: ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'],
  Portugais: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
};
const DAYS_FULL_MAP = {
  Français: { Lundi: 'Lundi', Mardi: 'Mardi', Mercredi: 'Mercredi', Jeudi: 'Jeudi', Vendredi: 'Vendredi', Samedi: 'Samedi', Dimanche: 'Dimanche' },
  Anglais: { Lundi: 'Monday', Mardi: 'Tuesday', Mercredi: 'Wednesday', Jeudi: 'Thursday', Vendredi: 'Friday', Samedi: 'Saturday', Dimanche: 'Sunday' },
  Espagnol: { Lundi: 'Lunes', Mardi: 'Martes', Mercredi: 'Miércoles', Jeudi: 'Jueves', Vendredi: 'Viernes', Samedi: 'Sábado', Dimanche: 'Domingo' },
  Italien: { Lundi: 'Lunedì', Mardi: 'Martedì', Mercredi: 'Mercoledì', Jeudi: 'Giovedì', Vendredi: 'Venerdì', Samedi: 'Sabato', Dimanche: 'Domenica' },
  Portugais: { Lundi: 'Segunda', Mardi: 'Terça', Mercredi: 'Quarta', Jeudi: 'Quinta', Vendredi: 'Sexta', Samedi: 'Sábado', Dimanche: 'Domingo' }
};
function tJour(j, langue) {
  return (DAYS_FULL_MAP[langue] && DAYS_FULL_MAP[langue][j]) || j;
}"""

if old_anchor in content:
    content = content.replace(old_anchor, new_anchor, 1)
    changes += 1
    print("OK 1/4 - DAYS_FULL_MAP et fonction tJour ajoutes")
else:
    print("ERREUR 1/4 - Ancre DAYS_SHORT_MAP non trouvee")

# 2. Traduire l'affichage des boutons Jours de repos (Parametres)
old_jours = """          {JOURS.map(j => (
            <button key={j} onClick={() => toggleJour(j)} style={{ padding: '7px 14px', borderRadius: 100, border: `1px solid ${form.joursRepos.includes(j) ? ACCENTS.glacier : C.iceLine}`, background: form.joursRepos.includes(j) ? ACCENTS.glacier + '18' : C.card, color: form.joursRepos.includes(j) ? ACCENTS.glacierDeep : C.ink, fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>{j}</button>
          ))}"""

new_jours = """          {JOURS.map(j => (
            <button key={j} onClick={() => toggleJour(j)} style={{ padding: '7px 14px', borderRadius: 100, border: `1px solid ${form.joursRepos.includes(j) ? ACCENTS.glacier : C.iceLine}`, background: form.joursRepos.includes(j) ? ACCENTS.glacier + '18' : C.card, color: form.joursRepos.includes(j) ? ACCENTS.glacierDeep : C.ink, fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>{tJour(j, langue)}</button>
          ))}"""

if old_jours in content:
    content = content.replace(old_jours, new_jours, 1)
    changes += 1
    print("OK 2/4 - Jours de repos traduits (Parametres)")
else:
    print("ERREUR 2/4 - Boutons Jours de repos non trouves")

# 3. Endonymes dans le selecteur de langue (Parametres)
old_select_params = """{field(tUI('labelLangueInterface', langue), <select style={inputStyle} value={form.langue} onChange={set('langue')}><option>Français</option><option>Anglais</option><option>Espagnol</option><option>Italien</option><option>Portugais</option></select>)}"""
new_select_params = """{field(tUI('labelLangueInterface', langue), <select style={inputStyle} value={form.langue} onChange={set('langue')}><option value="Français">Français</option><option value="Anglais">English</option><option value="Espagnol">Español</option><option value="Italien">Italiano</option><option value="Portugais">Português</option></select>)}"""

if old_select_params in content:
    content = content.replace(old_select_params, new_select_params, 1)
    changes += 1
    print("OK 3/4 - Endonymes appliques au selecteur de langue (Parametres)")
else:
    print("ERREUR 3/4 - Selecteur de langue (Parametres) non trouve")

# 4. Endonymes dans le selecteur de langue (AuthScreen)
old_select_auth = """<select value={authLangue} onChange={e => setAuthLangue(e.target.value)} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 8, padding: '5px 8px', fontSize: 12.5, color: C.inkSoft, background: '#fff' }}>
            <option>Français</option><option>Anglais</option><option>Espagnol</option><option>Italien</option><option>Portugais</option>
          </select>"""
new_select_auth = """<select value={authLangue} onChange={e => setAuthLangue(e.target.value)} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 8, padding: '5px 8px', fontSize: 12.5, color: C.inkSoft, background: '#fff' }}>
            <option value="Français">Français</option><option value="Anglais">English</option><option value="Espagnol">Español</option><option value="Italien">Italiano</option><option value="Portugais">Português</option>
          </select>"""

if old_select_auth in content:
    content = content.replace(old_select_auth, new_select_auth, 1)
    changes += 1
    print("OK 4/4 - Endonymes appliques au selecteur de langue (AuthScreen)")
else:
    print("ERREUR 4/4 - Selecteur de langue (AuthScreen) non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/{total} modifications appliquees.")
