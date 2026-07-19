with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

lang_anchors = [
    ("Français",
     "    btnCancel: 'Annuler', btnSave: 'Enregistrer', btnCreateReservation: 'Créer la réservation', btnDelete: 'Supprimer'\n  },",
     "    btnCancel: 'Annuler', btnSave: 'Enregistrer', btnCreateReservation: 'Créer la réservation', btnDelete: 'Supprimer',\n    totalReservations: 'réservations au total', searchClientStation: 'Rechercher un client, une station...',\n    filterAll: 'Tous', thHoraire: 'Horaire', thPaiement: 'Paiement',\n    noResults: 'Aucune réservation ne correspond à votre recherche.'\n  },"),
    ("Anglais",
     "    btnCancel: 'Cancel', btnSave: 'Save', btnCreateReservation: 'Create booking', btnDelete: 'Delete'\n  },",
     "    btnCancel: 'Cancel', btnSave: 'Save', btnCreateReservation: 'Create booking', btnDelete: 'Delete',\n    totalReservations: 'bookings total', searchClientStation: 'Search a client, a resort...',\n    filterAll: 'All', thHoraire: 'Time', thPaiement: 'Payment',\n    noResults: 'No booking matches your search.'\n  },"),
    ("Espagnol",
     "    btnCancel: 'Cancelar', btnSave: 'Guardar', btnCreateReservation: 'Crear reserva', btnDelete: 'Eliminar'\n  },",
     "    btnCancel: 'Cancelar', btnSave: 'Guardar', btnCreateReservation: 'Crear reserva', btnDelete: 'Eliminar',\n    totalReservations: 'reservas en total', searchClientStation: 'Buscar un cliente, una estación...',\n    filterAll: 'Todos', thHoraire: 'Horario', thPaiement: 'Pago',\n    noResults: 'Ninguna reserva coincide con tu búsqueda.'\n  },"),
    ("Italien",
     "    btnCancel: 'Annulla', btnSave: 'Salva', btnCreateReservation: 'Crea prenotazione', btnDelete: 'Elimina'\n  },",
     "    btnCancel: 'Annulla', btnSave: 'Salva', btnCreateReservation: 'Crea prenotazione', btnDelete: 'Elimina',\n    totalReservations: 'prenotazioni totali', searchClientStation: 'Cerca un cliente, una stazione...',\n    filterAll: 'Tutti', thHoraire: 'Orario', thPaiement: 'Pagamento',\n    noResults: 'Nessuna prenotazione corrisponde alla tua ricerca.'\n  },"),
    ("Portugais",
     "    btnCancel: 'Cancelar', btnSave: 'Salvar', btnCreateReservation: 'Criar reserva', btnDelete: 'Excluir'\n  }\n};",
     "    btnCancel: 'Cancelar', btnSave: 'Salvar', btnCreateReservation: 'Criar reserva', btnDelete: 'Excluir',\n    totalReservations: 'reservas no total', searchClientStation: 'Buscar um cliente, uma estação...',\n    filterAll: 'Todos', thHoraire: 'Horário', thPaiement: 'Pagamento',\n    noResults: 'Nenhuma reserva corresponde à sua busca.'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cles reservations ajoutees pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

old_view = """function ReservationsView({ reservations, onNew, onEdit, C, devise }) {
  const [filter, setFilter] = useState(''); const [statutFilter, setStatutFilter] = useState('Tous');
  const filtered = reservations.filter(r => (statutFilter === 'Tous' || r.statut === statutFilter)).filter(r => (r.nom + r.prenom + r.station).toLowerCase().includes(filter.toLowerCase())).sort((a, b) => b.date.localeCompare(a.date) || a.heureDebut.localeCompare(b.heureDebut));
  const th = { textAlign: 'left', fontSize: 12, fontWeight: 700, color: C.inkSoft, textTransform: 'uppercase', letterSpacing: '.03em', padding: '10px 14px', borderBottom: `1px solid ${C.iceLine}` };
  const td = { padding: '12px 14px', fontSize: 13.5, borderBottom: `1px solid ${C.iceLine}`, color: C.ink };
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
      <div className="header-row">
        <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>Réservations</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>{reservations.length} réservations au total</p></div>
        <button onClick={onNew} style={{ display: 'flex', alignItems: 'center', gap: 8, background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '10px 18px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}><Plus size={16} /> Nouvelle réservation</button>
      </div>
      <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
        <input placeholder="Rechercher un client, une station..." value={filter} onChange={e => setFilter(e.target.value)} style={{ flex: 1, border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px', fontSize: 14, background: C.card, color: C.ink }} />
        <select value={statutFilter} onChange={e => setStatutFilter(e.target.value)} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px', fontSize: 14, background: C.card, color: C.ink }}>{['Tous', ...STATUTS].map(s => <option key={s}>{s}</option>)}</select>
      </div>
      <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, overflow: 'hidden', overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead><tr><th style={th}>Client</th><th style={th}>Date</th><th style={th}>Horaire</th><th style={th}>Discipline</th><th style={th}>Station</th><th style={th}>Prix</th><th style={th}>Statut</th><th style={th}>Paiement</th><th style={th}></th></tr></thead>
          <tbody>
            {filtered.map(r => (
              <tr key={r.id} style={{ cursor: 'pointer' }} onClick={() => onEdit(r)}>
                <td style={td}>{r.prenom} {r.nom}</td><td style={td}>{fmtDateShort(r.date)}</td><td style={td}>{r.heureDebut}–{r.heureFin}</td>
                <td style={td}><div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}><Pill color={disciplineColor(r.discipline)}>{r.discipline}</Pill>{r.type && r.type !== 'Heure' && <Pill color={ACCENTS.amber}>{r.type}</Pill>}</div></td><td style={td}>{r.station}</td>
                <td style={{ ...td, fontWeight: 700, fontFamily: "'Space Grotesk', sans-serif" }}>{fmtEUR(r.prix, devise)}</td>
                <td style={td}><Pill color={statutColor(r.statut)}>{r.statut}</Pill></td>
                <td style={td}><Pill color={r.paiement === 'Payé' ? ACCENTS.green : C.inkSoft}>{r.paiement}</Pill></td>
                <td style={{ ...td, textAlign: 'right' }}><Pencil size={14} color={C.inkSoft} /></td>
              </tr>
            ))}
            {filtered.length === 0 && <tr><td colSpan={9} style={{ ...td, textAlign: 'center', color: C.inkSoft, padding: '32px 14px' }}>Aucune réservation ne correspond à votre recherche.</td></tr>}
          </tbody>
        </table>
      </div>
    </div>
  );
}"""

new_view = """function ReservationsView({ reservations, onNew, onEdit, C, devise, langue }) {
  const [filter, setFilter] = useState(''); const [statutFilter, setStatutFilter] = useState('Tous');
  const filtered = reservations.filter(r => (statutFilter === 'Tous' || r.statut === statutFilter)).filter(r => (r.nom + r.prenom + r.station).toLowerCase().includes(filter.toLowerCase())).sort((a, b) => b.date.localeCompare(a.date) || a.heureDebut.localeCompare(b.heureDebut));
  const th = { textAlign: 'left', fontSize: 12, fontWeight: 700, color: C.inkSoft, textTransform: 'uppercase', letterSpacing: '.03em', padding: '10px 14px', borderBottom: `1px solid ${C.iceLine}` };
  const td = { padding: '12px 14px', fontSize: 13.5, borderBottom: `1px solid ${C.iceLine}`, color: C.ink };
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
      <div className="header-row">
        <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>{tUI('reservations', langue)}</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>{reservations.length} {tUI('totalReservations', langue)}</p></div>
        <button onClick={onNew} style={{ display: 'flex', alignItems: 'center', gap: 8, background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '10px 18px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}><Plus size={16} /> {tUI('newReservation', langue)}</button>
      </div>
      <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
        <input placeholder={tUI('searchClientStation', langue)} value={filter} onChange={e => setFilter(e.target.value)} style={{ flex: 1, border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px', fontSize: 14, background: C.card, color: C.ink }} />
        <select value={statutFilter} onChange={e => setStatutFilter(e.target.value)} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px', fontSize: 14, background: C.card, color: C.ink }}>{['Tous', ...STATUTS].map(s => <option key={s}>{s === 'Tous' ? tUI('filterAll', langue) : s}</option>)}</select>
      </div>
      <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, overflow: 'hidden', overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead><tr><th style={th}>{tUI('thClient', langue)}</th><th style={th}>{tUI('fDate', langue)}</th><th style={th}>{tUI('thHoraire', langue)}</th><th style={th}>{tUI('fDiscipline', langue)}</th><th style={th}>{tUI('fStation', langue)}</th><th style={th}>{tUI('fPrix', langue)}</th><th style={th}>{tUI('fStatut', langue)}</th><th style={th}>{tUI('thPaiement', langue)}</th><th style={th}></th></tr></thead>
          <tbody>
            {filtered.map(r => (
              <tr key={r.id} style={{ cursor: 'pointer' }} onClick={() => onEdit(r)}>
                <td style={td}>{r.prenom} {r.nom}</td><td style={td}>{fmtDateShort(r.date)}</td><td style={td}>{r.heureDebut}–{r.heureFin}</td>
                <td style={td}><div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}><Pill color={disciplineColor(r.discipline)}>{r.discipline}</Pill>{r.type && r.type !== 'Heure' && <Pill color={ACCENTS.amber}>{r.type}</Pill>}</div></td><td style={td}>{r.station}</td>
                <td style={{ ...td, fontWeight: 700, fontFamily: "'Space Grotesk', sans-serif" }}>{fmtEUR(r.prix, devise)}</td>
                <td style={td}><Pill color={statutColor(r.statut)}>{r.statut}</Pill></td>
                <td style={td}><Pill color={r.paiement === 'Payé' ? ACCENTS.green : C.inkSoft}>{r.paiement}</Pill></td>
                <td style={{ ...td, textAlign: 'right' }}><Pencil size={14} color={C.inkSoft} /></td>
              </tr>
            ))}
            {filtered.length === 0 && <tr><td colSpan={9} style={{ ...td, textAlign: 'center', color: C.inkSoft, padding: '32px 14px' }}>{tUI('noResults', langue)}</td></tr>}
          </tbody>
        </table>
      </div>
    </div>
  );
}"""

if old_view in content:
    content = content.replace(old_view, new_view, 1)
    changes += 1
    print("OK - ReservationsView traduit")
else:
    print("ERREUR - ReservationsView non trouve")

# Ajouter la cle thClient (manquante dans le lot precedent) a chaque langue
lang_client = [
    ("Français", "thPaiement: 'Paiement',", "thPaiement: 'Paiement', thClient: 'Client',"),
    ("Anglais", "thPaiement: 'Payment',", "thPaiement: 'Payment', thClient: 'Client',"),
    ("Espagnol", "thPaiement: 'Pago',", "thPaiement: 'Pago', thClient: 'Cliente',"),
    ("Italien", "thPaiement: 'Pagamento',", "thPaiement: 'Pagamento', thClient: 'Cliente',"),
    ("Portugais", "thPaiement: 'Pagamento',", "thPaiement: 'Pagamento', thClient: 'Cliente',"),
]
for name, old, new in lang_client:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - thClient ajoute pour {name}")
    else:
        print(f"ERREUR - thPaiement non trouve pour {name}")

# Passer la langue depuis App()
old_call = """<ReservationsView reservations={reservations} onNew={() => openNew()} onEdit={openEdit} C={C} devise={settings.devise} />"""
new_call = """<ReservationsView reservations={reservations} onNew={() => openNew()} onEdit={openEdit} C={C} devise={settings.devise} langue={settings.langue} />"""

if old_call in content:
    content = content.replace(old_call, new_call, 1)
    changes += 1
    print("OK - Prop langue transmise a ReservationsView")
else:
    print("ERREUR - Appel ReservationsView non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes} modifications appliquees (Etape 5/N - Reservations).")
