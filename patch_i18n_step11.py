with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

lang_anchors = [
    ("Français",
     "    errFillEmailPassword: 'Merci de renseigner ton e-mail et ton mot de passe.'\n  },",
     "    errFillEmailPassword: 'Merci de renseigner ton e-mail et ton mot de passe.', loadingText: 'Chargement…'\n  },"),
    ("Anglais",
     "    errFillEmailPassword: 'Please enter your email and password.'\n  },",
     "    errFillEmailPassword: 'Please enter your email and password.', loadingText: 'Loading…'\n  },"),
    ("Espagnol",
     "    errFillEmailPassword: 'Por favor ingresa tu correo y contraseña.'\n  },",
     "    errFillEmailPassword: 'Por favor ingresa tu correo y contraseña.', loadingText: 'Cargando…'\n  },"),
    ("Italien",
     "    errFillEmailPassword: 'Inserisci la tua e-mail e password.'\n  },",
     "    errFillEmailPassword: 'Inserisci la tua e-mail e password.', loadingText: 'Caricamento…'\n  },"),
    ("Portugais",
     "    errFillEmailPassword: 'Por favor, informe seu e-mail e senha.'\n  }\n};",
     "    errFillEmailPassword: 'Por favor, informe seu e-mail e senha.', loadingText: 'Carregando…'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cle loadingText ajoutee pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

# Traduire les 2 boutons du menu mobile
old_mobile = """            <button onClick={() => { setTab('parametres'); setMobileMenuOpen(false); }} style={{ marginTop: 'auto', display: 'flex', alignItems: 'center', gap: 11, padding: '11px 12px', borderRadius: 9, border: 'none', cursor: 'pointer', textAlign: 'left', fontSize: 14.5, background: tab === 'parametres' ? 'rgba(255,255,255,0.1)' : 'transparent', color: tab === 'parametres' ? '#fff' : 'rgba(255,255,255,0.68)' }}>
              <SettingsIcon size={17} /> Paramètres
            </button>
            <button onClick={() => { setAuthed(false); setMobileMenuOpen(false); }} style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '11px 12px', borderRadius: 9, border: 'none', cursor: 'pointer', textAlign: 'left', fontSize: 14.5, background: 'transparent', color: 'rgba(255,255,255,0.5)' }}>
              <LogOut size={17} /> Déconnexion
            </button>"""

new_mobile = """            <button onClick={() => { setTab('parametres'); setMobileMenuOpen(false); }} style={{ marginTop: 'auto', display: 'flex', alignItems: 'center', gap: 11, padding: '11px 12px', borderRadius: 9, border: 'none', cursor: 'pointer', textAlign: 'left', fontSize: 14.5, background: tab === 'parametres' ? 'rgba(255,255,255,0.1)' : 'transparent', color: tab === 'parametres' ? '#fff' : 'rgba(255,255,255,0.68)' }}>
              <SettingsIcon size={17} /> {tUI('parametres', settings.langue)}
            </button>
            <button onClick={() => { setAuthed(false); setMobileMenuOpen(false); }} style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '11px 12px', borderRadius: 9, border: 'none', cursor: 'pointer', textAlign: 'left', fontSize: 14.5, background: 'transparent', color: 'rgba(255,255,255,0.5)' }}>
              <LogOut size={17} /> {tUI('deconnexion', settings.langue)}
            </button>"""

if old_mobile in content:
    content = content.replace(old_mobile, new_mobile, 1)
    changes += 1
    print("OK - Boutons menu mobile traduits")
else:
    print("ERREUR - Boutons menu mobile non trouves")

# Traduire le texte de chargement
old_loading = """          <div style={{ color: C.inkSoft, fontSize: 14 }}>Chargement…</div>"""
new_loading = """          <div style={{ color: C.inkSoft, fontSize: 14 }}>{tUI('loadingText', settings.langue)}</div>"""

if old_loading in content:
    content = content.replace(old_loading, new_loading, 1)
    changes += 1
    print("OK - Texte de chargement traduit")
else:
    print("ERREUR - Texte de chargement non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes} modifications appliquees (Etape 11/N - Menu mobile).")
