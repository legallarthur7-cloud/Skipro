with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

# 1. Remplacer la constante CRENEAUX fixe par une fonction basée sur les settings
old_creneaux = """const CRENEAUX = { 'Matin': ['09:00', '12:30'], 'Après-midi': ['13:30', '17:00'] };"""

new_creneaux = """function getCreneaux(settings) {
  return {
    'Matin': [settings.matinDebut || '09:00', settings.matinFin || '12:30'],
    'Après-midi': [settings.apresMidiDebut || '13:30', settings.apresMidiFin || '17:00']
  };
}"""

if old_creneaux in content:
    content = content.replace(old_creneaux, new_creneaux)
    changes += 1
    print("OK 1/4 - CRENEAUX transforme en fonction dynamique")
else:
    print("ERREUR 1/4 - Constante CRENEAUX non trouvee")

# 2. Injecter CRENEAUX local (basé sur settings) dans le composant de réservation
old_anchor = """  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }));

  const priceForType = useCallback((type, creneau, dateKey) => {"""

new_anchor = """  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }));
  const CRENEAUX = getCreneaux(settings);

  const priceForType = useCallback((type, creneau, dateKey) => {"""

if old_anchor in content:
    content = content.replace(old_anchor, new_anchor)
    changes += 1
    print("OK 2/4 - CRENEAUX local injecte dans le composant reservation")
else:
    print("ERREUR 2/4 - Ancre priceForType non trouvee")

# 3. Ajouter les 4 champs horaires par défaut dans DEFAULT_SETTINGS
old_settings = """const DEFAULT_SETTINGS = {
  nom: 'Moniteur ESF', email: 'contact@exemple.com', devise: 'EUR', langue: 'Français',
  fuseauHoraire: 'Europe/Paris',
  adresse: '', telephone: '', siret: '', profession: 'Moniteur de ski indépendant',
  iban: '', bic: '', banque: '',"""

new_settings = """const DEFAULT_SETTINGS = {
  nom: 'Moniteur ESF', email: 'contact@exemple.com', devise: 'EUR', langue: 'Français',
  fuseauHoraire: 'Europe/Paris',
  adresse: '', telephone: '', siret: '', profession: 'Moniteur de ski indépendant',
  iban: '', bic: '', banque: '',
  matinDebut: '09:00', matinFin: '12:30', apresMidiDebut: '13:30', apresMidiFin: '17:00',"""

if old_settings in content:
    content = content.replace(old_settings, new_settings)
    changes += 1
    print("OK 3/4 - Champs horaires ajoutes a DEFAULT_SETTINGS")
else:
    print("ERREUR 3/4 - Bloc DEFAULT_SETTINGS non trouve")

# 4. Ajouter la section "Horaires des demi-journées" dans Paramètres, avant "Jours de repos"
old_repos = """      {section('Jours de repos', (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
          {JOURS.map(j => ("""

new_repos = """      {section('Horaires des demi-journées', (
        <div className="form-grid-2">
          {field('Matin — début', <input type="time" style={inputStyle} value={form.matinDebut || '09:00'} onChange={set('matinDebut')} />)}
          {field('Matin — fin', <input type="time" style={inputStyle} value={form.matinFin || '12:30'} onChange={set('matinFin')} />)}
          {field('Après-midi — début', <input type="time" style={inputStyle} value={form.apresMidiDebut || '13:30'} onChange={set('apresMidiDebut')} />)}
          {field('Après-midi — fin', <input type="time" style={inputStyle} value={form.apresMidiFin || '17:00'} onChange={set('apresMidiFin')} />)}
        </div>
      ))}

      {section('Jours de repos', (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
          {JOURS.map(j => ("""

if old_repos in content:
    content = content.replace(old_repos, new_repos)
    changes += 1
    print("OK 4/4 - Section Horaires des demi-journees ajoutee")
else:
    print("ERREUR 4/4 - Bloc Jours de repos non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/4 modifications appliquees.")
