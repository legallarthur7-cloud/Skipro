with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

# 1. Ajouter le dictionnaire de traductions + fonction tUI, juste avant getCreneaux
old_anchor = """function getCreneaux(settings) {"""

new_anchor = """const UI_TRANSLATIONS = {
  Français: {
    dashboard: 'Tableau de bord', calendar: 'Calendrier', reservations: 'Réservations',
    clients: 'Clients', paiements: 'Paiements & Factures', stats: 'Statistiques',
    parametres: 'Paramètres', deconnexion: 'Déconnexion'
  },
  Anglais: {
    dashboard: 'Dashboard', calendar: 'Calendar', reservations: 'Bookings',
    clients: 'Clients', paiements: 'Payments & Invoices', stats: 'Statistics',
    parametres: 'Settings', deconnexion: 'Log out'
  },
  Espagnol: {
    dashboard: 'Panel', calendar: 'Calendario', reservations: 'Reservas',
    clients: 'Clientes', paiements: 'Pagos y Facturas', stats: 'Estadísticas',
    parametres: 'Ajustes', deconnexion: 'Cerrar sesión'
  },
  Italien: {
    dashboard: 'Bacheca', calendar: 'Calendario', reservations: 'Prenotazioni',
    clients: 'Clienti', paiements: 'Pagamenti e Fatture', stats: 'Statistiche',
    parametres: 'Impostazioni', deconnexion: 'Disconnetti'
  },
  Portugais: {
    dashboard: 'Painel', calendar: 'Calendário', reservations: 'Reservas',
    clients: 'Clientes', paiements: 'Pagamentos e Faturas', stats: 'Estatísticas',
    parametres: 'Configurações', deconnexion: 'Sair'
  }
};
function tUI(key, langue) {
  return (UI_TRANSLATIONS[langue] && UI_TRANSLATIONS[langue][key]) || UI_TRANSLATIONS['Français'][key] || key;
}

function getCreneaux(settings) {"""

if old_anchor in content:
    content = content.replace(old_anchor, new_anchor, 1)
    changes += 1
    print("OK 1/4 - Dictionnaire de traductions ajoute")
else:
    print("ERREUR 1/4 - Ancre getCreneaux non trouvee")

# 2. Traduire navItems + allTabLabel
old_nav = """  const navItems = [
    { id: 'dashboard', label: 'Tableau de bord', icon: LayoutDashboard },
    { id: 'calendar', label: 'Calendrier', icon: CalendarIcon },
    { id: 'reservations', label: 'Réservations', icon: Repeat },
    { id: 'clients', label: 'Clients', icon: Users },
    { id: 'paiements', label: 'Paiements & Factures', icon: FileText },
    { id: 'stats', label: 'Statistiques', icon: BarChart3 },
  ];

  if (!authChecked) return null;
  if (!authed) return <AuthScreen onAuth={() => setAuthed(true)} />;

  const allTabLabel = tab === 'parametres' ? 'Paramètres' : (navItems.find(n => n.id === tab)?.label || 'SkiPro');"""

new_nav = """  const navItems = [
    { id: 'dashboard', label: tUI('dashboard', settings.langue), icon: LayoutDashboard },
    { id: 'calendar', label: tUI('calendar', settings.langue), icon: CalendarIcon },
    { id: 'reservations', label: tUI('reservations', settings.langue), icon: Repeat },
    { id: 'clients', label: tUI('clients', settings.langue), icon: Users },
    { id: 'paiements', label: tUI('paiements', settings.langue), icon: FileText },
    { id: 'stats', label: tUI('stats', settings.langue), icon: BarChart3 },
  ];

  if (!authChecked) return null;
  if (!authed) return <AuthScreen onAuth={() => setAuthed(true)} />;

  const allTabLabel = tab === 'parametres' ? tUI('parametres', settings.langue) : (navItems.find(n => n.id === tab)?.label || 'SkiPro');"""

if old_nav in content:
    content = content.replace(old_nav, new_nav, 1)
    changes += 1
    print("OK 2/4 - navItems et allTabLabel traduits")
else:
    print("ERREUR 2/4 - Bloc navItems non trouve")

# 3. Traduire les boutons Paramètres / Déconnexion dans la sidebar
old_buttons = """        <button className="nav-btn" onClick={() => setTab('parametres')} style={{ marginTop: 'auto', borderRadius: 9, border: 'none', cursor: 'pointer', textAlign: 'left', background: tab === 'parametres' ? 'rgba(255,255,255,0.1)' : 'transparent', color: tab === 'parametres' ? '#fff' : 'rgba(255,255,255,0.68)' }}>
          <SettingsIcon size={16} /> Paramètres
        </button>
        <button className="nav-btn" onClick={() => supabase.auth.signOut()} style={{ borderRadius: 9, border: 'none', cursor: 'pointer', textAlign: 'left', background: 'transparent', color: 'rgba(255,255,255,0.5)' }}>
          <LogOut size={16} /> Déconnexion
        </button>"""

new_buttons = """        <button className="nav-btn" onClick={() => setTab('parametres')} style={{ marginTop: 'auto', borderRadius: 9, border: 'none', cursor: 'pointer', textAlign: 'left', background: tab === 'parametres' ? 'rgba(255,255,255,0.1)' : 'transparent', color: tab === 'parametres' ? '#fff' : 'rgba(255,255,255,0.68)' }}>
          <SettingsIcon size={16} /> {tUI('parametres', settings.langue)}
        </button>
        <button className="nav-btn" onClick={() => supabase.auth.signOut()} style={{ borderRadius: 9, border: 'none', cursor: 'pointer', textAlign: 'left', background: 'transparent', color: 'rgba(255,255,255,0.5)' }}>
          <LogOut size={16} /> {tUI('deconnexion', settings.langue)}
        </button>"""

if old_buttons in content:
    content = content.replace(old_buttons, new_buttons, 1)
    changes += 1
    print("OK 3/4 - Boutons Parametres/Deconnexion traduits")
else:
    print("ERREUR 3/4 - Boutons sidebar non trouves")

# 4. Mettre a jour le selecteur de langue dans Parametres (5 langues au lieu de 2)
old_select = """          {field('Langue', <select style={inputStyle} value={form.langue} onChange={set('langue')}><option>Français</option><option>English</option></select>)}"""

new_select = """          {field('Langue de l\\'interface', <select style={inputStyle} value={form.langue} onChange={set('langue')}><option>Français</option><option>Anglais</option><option>Espagnol</option><option>Italien</option><option>Portugais</option></select>)}"""

if old_select in content:
    content = content.replace(old_select, new_select, 1)
    changes += 1
    print("OK 4/4 - Selecteur de langue mis a jour (5 langues)")
else:
    print("ERREUR 4/4 - Selecteur de langue non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/4 modifications appliquees (Etape 1/N - menu de navigation).")
