with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0
total = 7

# 1. Ajouter les cles de traduction (bouton + etats de chargement/erreur)
lang_anchors = [
    ("Français",
     "    errFillEmailPassword: 'Merci de renseigner ton e-mail et ton mot de passe.', loadingText: 'Chargement…'\n  },",
     "    errFillEmailPassword: 'Merci de renseigner ton e-mail et ton mot de passe.', loadingText: 'Chargement…',\n    btnManageSubscription: 'Gérer mon abonnement', errPortalUnavailable: \"Impossible d'ouvrir la gestion de l'abonnement pour le moment.\"\n  },"),
    ("Anglais",
     "    errFillEmailPassword: 'Please enter your email and password.', loadingText: 'Loading…'\n  },",
     "    errFillEmailPassword: 'Please enter your email and password.', loadingText: 'Loading…',\n    btnManageSubscription: 'Manage subscription', errPortalUnavailable: 'Unable to open subscription management right now.'\n  },"),
    ("Espagnol",
     "    errFillEmailPassword: 'Por favor ingresa tu correo y contraseña.', loadingText: 'Cargando…'\n  },",
     "    errFillEmailPassword: 'Por favor ingresa tu correo y contraseña.', loadingText: 'Cargando…',\n    btnManageSubscription: 'Gestionar suscripción', errPortalUnavailable: 'No se puede abrir la gestión de la suscripción en este momento.'\n  },"),
    ("Italien",
     "    errFillEmailPassword: 'Inserisci la tua e-mail e password.', loadingText: 'Caricamento…'\n  },",
     "    errFillEmailPassword: 'Inserisci la tua e-mail e password.', loadingText: 'Caricamento…',\n    btnManageSubscription: 'Gestisci abbonamento', errPortalUnavailable: \"Impossibile aprire la gestione dell'abbonamento al momento.\"\n  },"),
    ("Portugais",
     "    errFillEmailPassword: 'Por favor, informe seu e-mail e senha.', loadingText: 'Carregando…'\n  }\n};",
     "    errFillEmailPassword: 'Por favor, informe seu e-mail e senha.', loadingText: 'Carregando…',\n    btnManageSubscription: 'Gerenciar assinatura', errPortalUnavailable: 'Não foi possível abrir o gerenciamento da assinatura no momento.'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cles portail ajoutees pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

# 2. Ajouter un state portalLoading et la fonction handlePortal, juste apres handleSubscribe
old_handle = """  const handleSubscribe = async () => {
    setSubLoading(true);
    try {
      const { data: { user } } = await supabase.auth.getUser();
      const res = await fetch('/api/create-checkout-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: form.email, telephone: form.telephone || '', userId: user?.id || '' }),
      });
      const data = await res.json();
      if (data.url) window.location.href = data.url;
      else { alert('Erreur : ' + (data.error || 'inconnue')); setSubLoading(false); }
    } catch (e) {
      alert('Erreur de connexion à Stripe.');
      setSubLoading(false);
    }
  };"""

new_handle = """  const handleSubscribe = async () => {
    setSubLoading(true);
    try {
      const { data: { user } } = await supabase.auth.getUser();
      const res = await fetch('/api/create-checkout-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: form.email, telephone: form.telephone || '', userId: user?.id || '' }),
      });
      const data = await res.json();
      if (data.url) window.location.href = data.url;
      else { alert('Erreur : ' + (data.error || 'inconnue')); setSubLoading(false); }
    } catch (e) {
      alert('Erreur de connexion à Stripe.');
      setSubLoading(false);
    }
  };

  const handleManageSubscription = async () => {
    setPortalLoading(true);
    try {
      const res = await fetch('/api/create-portal-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: form.email }),
      });
      const data = await res.json();
      if (data.url) window.location.href = data.url;
      else { alert(tUI('errPortalUnavailable', langue)); setPortalLoading(false); }
    } catch (e) {
      alert(tUI('errPortalUnavailable', langue));
      setPortalLoading(false);
    }
  };"""

if old_handle in content:
    content = content.replace(old_handle, new_handle, 1)
    changes += 1
    print("OK - Fonction handleManageSubscription ajoutee")
else:
    print("ERREUR - handleSubscribe non trouve pour insertion")

# 3. Ajouter le state portalLoading
old_state = """  const [subLoading, setSubLoading] = useState(false);"""
new_state = """  const [subLoading, setSubLoading] = useState(false);
  const [portalLoading, setPortalLoading] = useState(false);"""

if old_state in content:
    content = content.replace(old_state, new_state, 1)
    changes += 1
    print("OK - State portalLoading ajoute")
else:
    print("ERREUR - State subLoading non trouve")

# 4. Remplacer le badge "Abonnement actif" par badge + bouton Gerer
old_badge = """          {subscribed ? (
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, background: '#E6F4EA', color: '#1E7A3D', borderRadius: 9, padding: '11px 18px', fontSize: 14, fontWeight: 600 }}>
              ✓ {tUI('activeSubscription', langue)}
            </div>
          ) : ("""

new_badge = """          {subscribed ? (
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, flexWrap: 'wrap' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, background: '#E6F4EA', color: '#1E7A3D', borderRadius: 9, padding: '11px 18px', fontSize: 14, fontWeight: 600 }}>
                ✓ {tUI('activeSubscription', langue)}
              </div>
              <button onClick={handleManageSubscription} disabled={portalLoading} style={{ background: 'none', border: `1px solid ${C.iceLine}`, color: C.ink, borderRadius: 9, padding: '11px 18px', fontSize: 14, fontWeight: 600, cursor: portalLoading ? 'default' : 'pointer', opacity: portalLoading ? 0.7 : 1 }}>
                {portalLoading ? tUI('loadingWait', langue) : tUI('btnManageSubscription', langue)}
              </button>
            </div>
          ) : ("""

if old_badge in content:
    content = content.replace(old_badge, new_badge, 1)
    changes += 1
    print("OK - Bouton Gerer mon abonnement ajoute a cote du badge")
else:
    print("ERREUR - Badge Abonnement actif non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/{total} modifications appliquees.")
