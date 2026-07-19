with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0
total = 7

# 1. Ajouter le champ slug aux parametres par defaut
old_settings = """  adresse: '', telephone: '', siret: '', profession: 'Moniteur de ski indépendant',
  iban: '', bic: '', banque: '',"""
new_settings = """  adresse: '', telephone: '', siret: '', profession: 'Moniteur de ski indépendant',
  iban: '', bic: '', banque: '', slug: '',"""

if old_settings in content:
    content = content.replace(old_settings, new_settings, 1)
    changes += 1
    print("OK 1/7 - Champ slug ajoute a DEFAULT_SETTINGS")
else:
    print("ERREUR 1/7 - DEFAULT_SETTINGS non trouve")

# 2-6. Ajouter les cles de traduction
lang_anchors = [
    ("Français",
     "    errPortalUnavailable: \"Impossible d'ouvrir la gestion de l'abonnement pour le moment.\"\n  },",
     "    errPortalUnavailable: \"Impossible d'ouvrir la gestion de l'abonnement pour le moment.\",\n    sectionLienReservation: 'Lien de réservation en ligne', labelSlug: 'Identifiant personnalisé',\n    yourPublicLink: 'Ton lien public', slugTaken: 'Cet identifiant est déjà pris, choisis-en un autre.',\n    slugSaved: 'Lien enregistré ✓'\n  },"),
    ("Anglais",
     "    errPortalUnavailable: 'Unable to open subscription management right now.'\n  },",
     "    errPortalUnavailable: 'Unable to open subscription management right now.',\n    sectionLienReservation: 'Online booking link', labelSlug: 'Custom handle',\n    yourPublicLink: 'Your public link', slugTaken: 'This handle is already taken, choose another one.',\n    slugSaved: 'Link saved ✓'\n  },"),
    ("Espagnol",
     "    errPortalUnavailable: 'No se puede abrir la gestión de la suscripción en este momento.'\n  },",
     "    errPortalUnavailable: 'No se puede abrir la gestión de la suscripción en este momento.',\n    sectionLienReservation: 'Enlace de reserva en línea', labelSlug: 'Identificador personalizado',\n    yourPublicLink: 'Tu enlace público', slugTaken: 'Este identificador ya está en uso, elige otro.',\n    slugSaved: 'Enlace guardado ✓'\n  },"),
    ("Italien",
     "    errPortalUnavailable: \"Impossibile aprire la gestione dell'abbonamento al momento.\"\n  },",
     "    errPortalUnavailable: \"Impossibile aprire la gestione dell'abbonamento al momento.\",\n    sectionLienReservation: 'Link di prenotazione online', labelSlug: 'Identificativo personalizzato',\n    yourPublicLink: 'Il tuo link pubblico', slugTaken: 'Questo identificativo è già in uso, scegline un altro.',\n    slugSaved: 'Link salvato ✓'\n  },"),
    ("Portugais",
     "    errPortalUnavailable: 'Não foi possível abrir o gerenciamento da assinatura no momento.'\n  }\n};",
     "    errPortalUnavailable: 'Não foi possível abrir o gerenciamento da assinatura no momento.',\n    sectionLienReservation: 'Link de reserva online', labelSlug: 'Identificador personalizado',\n    yourPublicLink: 'Seu link público', slugTaken: 'Este identificador já está em uso, escolha outro.',\n    slugSaved: 'Link salvo ✓'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cles slug ajoutees pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

# 7. Ajouter la section dans ParametresView, entre Coordonnees et Coordonnees bancaires
old_section = """        <div style={{ marginTop: 14 }}>
          {field(tUI('labelAdressePostale', langue), <input style={inputStyle} value={form.adresse || ''} onChange={set('adresse')} placeholder="Numéro, rue, code postal, ville" />)}
        </div>
        </>
      ))}

      {section(tUI('sectionBanque', langue), ("""

new_section = """        <div style={{ marginTop: 14 }}>
          {field(tUI('labelAdressePostale', langue), <input style={inputStyle} value={form.adresse || ''} onChange={set('adresse')} placeholder="Numéro, rue, code postal, ville" />)}
        </div>
        </>
      ))}

      {section(tUI('sectionLienReservation', langue), (
        <div>
          {field(tUI('labelSlug', langue), <input style={inputStyle} value={form.slug || ''} onChange={e => setForm(f => ({ ...f, slug: e.target.value.toLowerCase().replace(/[^a-z0-9-]/g, '') }))} placeholder="arthur" />)}
          <div style={{ fontSize: 12.5, color: C.inkSoft, marginTop: 8 }}>
            {tUI('yourPublicLink', langue)} : <strong style={{ color: C.navy }}>skipro-app.com/{form.slug || '...'}</strong>
          </div>
        </div>
      ))}

      {section(tUI('sectionBanque', langue), ("""

if old_section in content:
    content = content.replace(old_section, new_section, 1)
    changes += 1
    print("OK - Section Lien de reservation ajoutee dans Parametres")
else:
    print("ERREUR - Ancre section Coordonnees/Banque non trouvee")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/{total} modifications appliquees (Etape 1 - champ slug).")
