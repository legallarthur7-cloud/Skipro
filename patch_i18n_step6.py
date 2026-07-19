with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

lang_anchors = [
    ("Français",
     "    noResults: 'Aucune réservation ne correspond à votre recherche.'\n  },",
     "    noResults: 'Aucune réservation ne correspond à votre recherche.',\n    lessonsFollowed: 'Cours suivis', totalHours: 'Heures totales', totalSpent: 'Dépense totale',\n    preferredDiscipline: 'Discipline préférée', lessonHistory: 'Historique des cours',\n    documents: 'Documents', noDocuments: 'Aucun document pour ce client.',\n    clientsInCrm: 'clients dans votre CRM', searchClient: 'Rechercher un client...',\n    miniLessons: 'Cours', miniHours: 'Heures', miniSpent: 'Dépensé',\n    noClientsMatch: 'Aucun client ne correspond à votre recherche.'\n  },"),
    ("Anglais",
     "    noResults: 'No booking matches your search.'\n  },",
     "    noResults: 'No booking matches your search.',\n    lessonsFollowed: 'Lessons taken', totalHours: 'Total hours', totalSpent: 'Total spent',\n    preferredDiscipline: 'Preferred discipline', lessonHistory: 'Lesson history',\n    documents: 'Documents', noDocuments: 'No documents for this client.',\n    clientsInCrm: 'clients in your CRM', searchClient: 'Search a client...',\n    miniLessons: 'Lessons', miniHours: 'Hours', miniSpent: 'Spent',\n    noClientsMatch: 'No client matches your search.'\n  },"),
    ("Espagnol",
     "    noResults: 'Ninguna reserva coincide con tu búsqueda.'\n  },",
     "    noResults: 'Ninguna reserva coincide con tu búsqueda.',\n    lessonsFollowed: 'Clases realizadas', totalHours: 'Horas totales', totalSpent: 'Gasto total',\n    preferredDiscipline: 'Disciplina preferida', lessonHistory: 'Historial de clases',\n    documents: 'Documentos', noDocuments: 'Ningún documento para este cliente.',\n    clientsInCrm: 'clientes en tu CRM', searchClient: 'Buscar un cliente...',\n    miniLessons: 'Clases', miniHours: 'Horas', miniSpent: 'Gastado',\n    noClientsMatch: 'Ningún cliente coincide con tu búsqueda.'\n  },"),
    ("Italien",
     "    noResults: 'Nessuna prenotazione corrisponde alla tua ricerca.'\n  },",
     "    noResults: 'Nessuna prenotazione corrisponde alla tua ricerca.',\n    lessonsFollowed: 'Lezioni seguite', totalHours: 'Ore totali', totalSpent: 'Spesa totale',\n    preferredDiscipline: 'Disciplina preferita', lessonHistory: 'Storico lezioni',\n    documents: 'Documenti', noDocuments: 'Nessun documento per questo cliente.',\n    clientsInCrm: 'clienti nel tuo CRM', searchClient: 'Cerca un cliente...',\n    miniLessons: 'Lezioni', miniHours: 'Ore', miniSpent: 'Speso',\n    noClientsMatch: 'Nessun cliente corrisponde alla tua ricerca.'\n  },"),
    ("Portugais",
     "    noResults: 'Nenhuma reserva corresponde à sua busca.'\n  }\n};",
     "    noResults: 'Nenhuma reserva corresponde à sua busca.',\n    lessonsFollowed: 'Aulas realizadas', totalHours: 'Horas totais', totalSpent: 'Total gasto',\n    preferredDiscipline: 'Modalidade preferida', lessonHistory: 'Histórico de aulas',\n    documents: 'Documentos', noDocuments: 'Nenhum documento para este cliente.',\n    clientsInCrm: 'clientes no seu CRM', searchClient: 'Buscar um cliente...',\n    miniLessons: 'Aulas', miniHours: 'Horas', miniSpent: 'Gasto',\n    noClientsMatch: 'Nenhum cliente corresponde à sua busca.'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cles clients ajoutees pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

# Reecrire ClientModal
old_cm = """function ClientModal({ client, onClose, C, devise }) {
  const history = [...client.reservations].sort((a, b) => b.date.localeCompare(a.date));
  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(10,18,27,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100, padding: 20 }} onClick={onClose}>
      <div style={{ background: C.snow, borderRadius: 18, width: '100%', maxWidth: 640, maxHeight: '86vh', overflowY: 'auto' }} onClick={e => e.stopPropagation()}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '18px 24px', borderBottom: `1px solid ${C.iceLine}`, position: 'sticky', top: 0, background: C.snow }}>
          <div><div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 18, color: C.navy }}>{client.prenom} {client.nom}</div><div style={{ fontSize: 13, color: C.inkSoft, marginTop: 2 }}>{client.telephone} · {client.email}</div></div>
          <button onClick={onClose} style={{ background: 'none', border: 'none', cursor: 'pointer', color: C.inkSoft }}><X size={20} /></button>
        </div>
        <div style={{ padding: 24, display: 'flex', flexDirection: 'column', gap: 20 }}>
          <div className="kpi-grid-3">
            <KpiCard C={C} label="Cours suivis" value={client.nbCours} icon={Repeat} accent={ACCENTS.blue} />
            <KpiCard C={C} label="Heures totales" value={`${client.totalHeures.toFixed(1)}h`} icon={TrendingUp} accent={ACCENTS.green} />
            <KpiCard C={C} label="Dépense totale" value={fmtEUR(client.totalDepense, devise)} icon={Euro} accent={ACCENTS.amber} />
          </div>
          <div className="form-grid-2" style={{ fontSize: 13.5, color: C.ink }}>
            <div><span style={{ color: C.inkSoft }}>Nationalité :</span> {client.nationalite || '—'}</div>
            <div><span style={{ color: C.inkSoft }}>Langue :</span> {client.langue || '—'}</div>
            <div><span style={{ color: C.inkSoft }}>Niveau :</span> {client.niveau}</div>
            <div><span style={{ color: C.inkSoft }}>Discipline préférée :</span> {client.preference}</div>
          </div>
          {client.notes.length > 0 && (
            <div><div style={{ fontSize: 13, fontWeight: 700, color: C.navy, marginBottom: 8 }}>Notes privées</div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>{client.notes.map((n, i) => <div key={i} style={{ fontSize: 13, color: C.inkSoft, background: C.snowDim, borderRadius: 8, padding: '8px 10px' }}>{n}</div>)}</div>
            </div>
          )}
          <div>
            <div style={{ fontSize: 13, fontWeight: 700, color: C.navy, marginBottom: 8 }}>Historique des cours</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              {history.map(r => (
                <div key={r.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '9px 12px', border: `1px solid ${C.iceLine}`, borderRadius: 9 }}>
                  <div><div style={{ fontSize: 13, fontWeight: 600, color: C.ink }}>{fmtDateShort(r.date)} · {r.heureDebut}–{r.heureFin}</div><div style={{ fontSize: 12, color: C.inkSoft }}>{r.station} · {r.niveau}</div></div>
                  <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}><Pill color={disciplineColor(r.discipline)}>{r.discipline}</Pill><span style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 13.5, color: C.ink }}>{fmtEUR(r.prix, devise)}</span></div>
                </div>
              ))}
            </div>
          </div>
          <div>
            <div style={{ fontSize: 13, fontWeight: 700, color: C.navy, marginBottom: 8 }}>Documents</div>
            <div style={{ fontSize: 13, color: C.inkSoft, background: C.snowDim, borderRadius: 9, padding: '14px', textAlign: 'center' }}>Aucun document pour ce client.</div>
          </div>
        </div>
      </div>
    </div>
  );
}"""

new_cm = """function ClientModal({ client, onClose, C, devise, langue }) {
  const history = [...client.reservations].sort((a, b) => b.date.localeCompare(a.date));
  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(10,18,27,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100, padding: 20 }} onClick={onClose}>
      <div style={{ background: C.snow, borderRadius: 18, width: '100%', maxWidth: 640, maxHeight: '86vh', overflowY: 'auto' }} onClick={e => e.stopPropagation()}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '18px 24px', borderBottom: `1px solid ${C.iceLine}`, position: 'sticky', top: 0, background: C.snow }}>
          <div><div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 18, color: C.navy }}>{client.prenom} {client.nom}</div><div style={{ fontSize: 13, color: C.inkSoft, marginTop: 2 }}>{client.telephone} · {client.email}</div></div>
          <button onClick={onClose} style={{ background: 'none', border: 'none', cursor: 'pointer', color: C.inkSoft }}><X size={20} /></button>
        </div>
        <div style={{ padding: 24, display: 'flex', flexDirection: 'column', gap: 20 }}>
          <div className="kpi-grid-3">
            <KpiCard C={C} label={tUI('lessonsFollowed', langue)} value={client.nbCours} icon={Repeat} accent={ACCENTS.blue} />
            <KpiCard C={C} label={tUI('totalHours', langue)} value={`${client.totalHeures.toFixed(1)}h`} icon={TrendingUp} accent={ACCENTS.green} />
            <KpiCard C={C} label={tUI('totalSpent', langue)} value={fmtEUR(client.totalDepense, devise)} icon={Euro} accent={ACCENTS.amber} />
          </div>
          <div className="form-grid-2" style={{ fontSize: 13.5, color: C.ink }}>
            <div><span style={{ color: C.inkSoft }}>{tUI('fNationalite', langue)} :</span> {client.nationalite || '—'}</div>
            <div><span style={{ color: C.inkSoft }}>{tUI('fLangueParlee', langue)} :</span> {client.langue || '—'}</div>
            <div><span style={{ color: C.inkSoft }}>{tUI('fNiveau', langue)} :</span> {client.niveau}</div>
            <div><span style={{ color: C.inkSoft }}>{tUI('preferredDiscipline', langue)} :</span> {client.preference}</div>
          </div>
          {client.notes.length > 0 && (
            <div><div style={{ fontSize: 13, fontWeight: 700, color: C.navy, marginBottom: 8 }}>{tUI('fNotes', langue)}</div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>{client.notes.map((n, i) => <div key={i} style={{ fontSize: 13, color: C.inkSoft, background: C.snowDim, borderRadius: 8, padding: '8px 10px' }}>{n}</div>)}</div>
            </div>
          )}
          <div>
            <div style={{ fontSize: 13, fontWeight: 700, color: C.navy, marginBottom: 8 }}>{tUI('lessonHistory', langue)}</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              {history.map(r => (
                <div key={r.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '9px 12px', border: `1px solid ${C.iceLine}`, borderRadius: 9 }}>
                  <div><div style={{ fontSize: 13, fontWeight: 600, color: C.ink }}>{fmtDateShort(r.date)} · {r.heureDebut}–{r.heureFin}</div><div style={{ fontSize: 12, color: C.inkSoft }}>{r.station} · {r.niveau}</div></div>
                  <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}><Pill color={disciplineColor(r.discipline)}>{r.discipline}</Pill><span style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 13.5, color: C.ink }}>{fmtEUR(r.prix, devise)}</span></div>
                </div>
              ))}
            </div>
          </div>
          <div>
            <div style={{ fontSize: 13, fontWeight: 700, color: C.navy, marginBottom: 8 }}>{tUI('documents', langue)}</div>
            <div style={{ fontSize: 13, color: C.inkSoft, background: C.snowDim, borderRadius: 9, padding: '14px', textAlign: 'center' }}>{tUI('noDocuments', langue)}</div>
          </div>
        </div>
      </div>
    </div>
  );
}"""

if old_cm in content:
    content = content.replace(old_cm, new_cm, 1)
    changes += 1
    print("OK - ClientModal traduit")
else:
    print("ERREUR - ClientModal non trouve")

# Reecrire ClientsView
old_cv = """function ClientsView({ reservations, C, devise, subscribed }) {
  const [search, setSearch] = useState(''); const [selected, setSelected] = useState(null);
  const clients = useMemo(() => aggregateClients(reservations), [reservations]);
  const filtered = clients.filter(c => (c.prenom + c.nom).toLowerCase().includes(search.toLowerCase()));
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
      <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>Clients</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>{clients.length} clients dans votre CRM</p></div>
      <BlurGate subscribed={subscribed} C={C}>
      <div style={{ position: 'relative', maxWidth: 360 }}>
        <Search size={15} style={{ position: 'absolute', left: 12, top: 11, color: C.inkSoft }} />
        <input placeholder="Rechercher un client..." value={search} onChange={e => setSearch(e.target.value)} style={{ width: '100%', border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px 9px 34px', fontSize: 14, background: C.card, color: C.ink }} />
      </div>
      <div className="clients-grid">
        {filtered.map(c => (
          <div key={c.key} onClick={() => setSelected(c)} style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '18px 20px', cursor: 'pointer' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <div style={{ fontSize: 15, fontWeight: 700, color: C.navy }}>{c.prenom} {c.nom}</div>
              <Pill color={disciplineColor(c.preference)}>{c.preference}</Pill>
            </div>
            <div style={{ fontSize: 12.5, color: C.inkSoft, marginTop: 4 }}>{c.nationalite} · {c.niveau}</div>
            <div style={{ display: 'flex', gap: 16, marginTop: 14 }}>
              <div><div style={{ fontSize: 11.5, color: C.inkSoft }}>Cours</div><div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 16, color: C.ink }}>{c.nbCours}</div></div>
              <div><div style={{ fontSize: 11.5, color: C.inkSoft }}>Heures</div><div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 16, color: C.ink }}>{c.totalHeures.toFixed(1)}h</div></div>
              <div><div style={{ fontSize: 11.5, color: C.inkSoft }}>Dépensé</div><div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 16, color: ACCENTS.green }}>{fmtEUR(c.totalDepense, devise)}</div></div>
            </div>
          </div>
        ))}
        {filtered.length === 0 && <div style={{ color: C.inkSoft, fontSize: 14 }}>Aucun client ne correspond à votre recherche.</div>}
      </div>
      </BlurGate>
      {selected && <ClientModal client={selected} onClose={() => setSelected(null)} C={C} devise={devise} />}
    </div>
  );
}"""

new_cv = """function ClientsView({ reservations, C, devise, subscribed, langue }) {
  const [search, setSearch] = useState(''); const [selected, setSelected] = useState(null);
  const clients = useMemo(() => aggregateClients(reservations), [reservations]);
  const filtered = clients.filter(c => (c.prenom + c.nom).toLowerCase().includes(search.toLowerCase()));
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
      <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>{tUI('clients', langue)}</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>{clients.length} {tUI('clientsInCrm', langue)}</p></div>
      <BlurGate subscribed={subscribed} C={C}>
      <div style={{ position: 'relative', maxWidth: 360 }}>
        <Search size={15} style={{ position: 'absolute', left: 12, top: 11, color: C.inkSoft }} />
        <input placeholder={tUI('searchClient', langue)} value={search} onChange={e => setSearch(e.target.value)} style={{ width: '100%', border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px 9px 34px', fontSize: 14, background: C.card, color: C.ink }} />
      </div>
      <div className="clients-grid">
        {filtered.map(c => (
          <div key={c.key} onClick={() => setSelected(c)} style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '18px 20px', cursor: 'pointer' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <div style={{ fontSize: 15, fontWeight: 700, color: C.navy }}>{c.prenom} {c.nom}</div>
              <Pill color={disciplineColor(c.preference)}>{c.preference}</Pill>
            </div>
            <div style={{ fontSize: 12.5, color: C.inkSoft, marginTop: 4 }}>{c.nationalite} · {c.niveau}</div>
            <div style={{ display: 'flex', gap: 16, marginTop: 14 }}>
              <div><div style={{ fontSize: 11.5, color: C.inkSoft }}>{tUI('miniLessons', langue)}</div><div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 16, color: C.ink }}>{c.nbCours}</div></div>
              <div><div style={{ fontSize: 11.5, color: C.inkSoft }}>{tUI('miniHours', langue)}</div><div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 16, color: C.ink }}>{c.totalHeures.toFixed(1)}h</div></div>
              <div><div style={{ fontSize: 11.5, color: C.inkSoft }}>{tUI('miniSpent', langue)}</div><div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 16, color: ACCENTS.green }}>{fmtEUR(c.totalDepense, devise)}</div></div>
            </div>
          </div>
        ))}
        {filtered.length === 0 && <div style={{ color: C.inkSoft, fontSize: 14 }}>{tUI('noClientsMatch', langue)}</div>}
      </div>
      </BlurGate>
      {selected && <ClientModal client={selected} onClose={() => setSelected(null)} C={C} devise={devise} langue={langue} />}
    </div>
  );
}"""

if old_cv in content:
    content = content.replace(old_cv, new_cv, 1)
    changes += 1
    print("OK - ClientsView traduit")
else:
    print("ERREUR - ClientsView non trouve")

# Passer la langue depuis App()
old_call = """<ClientsView reservations={reservations} C={C} devise={settings.devise} subscribed={subscribed} />"""
new_call = """<ClientsView reservations={reservations} C={C} devise={settings.devise} subscribed={subscribed} langue={settings.langue} />"""

if old_call in content:
    content = content.replace(old_call, new_call, 1)
    changes += 1
    print("OK - Prop langue transmise a ClientsView")
else:
    print("ERREUR - Appel ClientsView non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes} modifications appliquees (Etape 6/N - Clients).")
