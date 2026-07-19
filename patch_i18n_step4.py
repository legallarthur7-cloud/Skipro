with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

# Ajouter les nouvelles cles de traduction pour chaque langue
lang_anchors = [
    ("Français",
     "    calendarTitle: 'Calendrier', viewDay: 'Jour', viewWeek: 'Semaine', viewMonth: 'Mois', today: \"Aujourd'hui\", lessonsCount: 'cours'\n  },",
     "    calendarTitle: 'Calendrier', viewDay: 'Jour', viewWeek: 'Semaine', viewMonth: 'Mois', today: \"Aujourd'hui\", lessonsCount: 'cours',\n    modalEditTitle: 'Modifier la réservation', highSeason: 'Haute saison', lowSeason: 'Basse saison',\n    engHeure: 'Heure', engDemiJournee: 'Demi-journée', engJournee: 'Journée',\n    crenMatin: 'Matin', crenApresMidi: 'Après-midi',\n    fPrenom: 'Prénom', fNom: 'Nom', fTelephone: 'Téléphone', fEmail: 'E-mail', fNationalite: 'Nationalité',\n    fLangueParlee: 'Langue parlée', fAge: 'Âge', fNiveau: 'Niveau', fDiscipline: 'Discipline',\n    fNbPersonnes: 'Nombre de personnes', fStation: 'Station', fPointRdv: 'Point de rendez-vous',\n    fDate: 'Date', fHeureDebut: 'Heure de début', fHeureFin: 'Heure de fin', fDuree: 'Durée', fPrix: 'Prix',\n    suggestedRate: 'Tarif suggéré', fStatut: 'Statut', fModePaiement: 'Mode de règlement',\n    fStatutPaiement: 'Statut du paiement', fNotes: 'Notes privées',\n    btnCancel: 'Annuler', btnSave: 'Enregistrer', btnCreateReservation: 'Créer la réservation', btnDelete: 'Supprimer'\n  },"),
    ("Anglais",
     "    calendarTitle: 'Calendar', viewDay: 'Day', viewWeek: 'Week', viewMonth: 'Month', today: 'Today', lessonsCount: 'lessons'\n  },",
     "    calendarTitle: 'Calendar', viewDay: 'Day', viewWeek: 'Week', viewMonth: 'Month', today: 'Today', lessonsCount: 'lessons',\n    modalEditTitle: 'Edit booking', highSeason: 'High season', lowSeason: 'Low season',\n    engHeure: 'Hour', engDemiJournee: 'Half-day', engJournee: 'Full day',\n    crenMatin: 'Morning', crenApresMidi: 'Afternoon',\n    fPrenom: 'First name', fNom: 'Last name', fTelephone: 'Phone', fEmail: 'Email', fNationalite: 'Nationality',\n    fLangueParlee: 'Spoken language', fAge: 'Age', fNiveau: 'Level', fDiscipline: 'Discipline',\n    fNbPersonnes: 'Number of people', fStation: 'Resort', fPointRdv: 'Meeting point',\n    fDate: 'Date', fHeureDebut: 'Start time', fHeureFin: 'End time', fDuree: 'Duration', fPrix: 'Price',\n    suggestedRate: 'Suggested rate', fStatut: 'Status', fModePaiement: 'Payment method',\n    fStatutPaiement: 'Payment status', fNotes: 'Private notes',\n    btnCancel: 'Cancel', btnSave: 'Save', btnCreateReservation: 'Create booking', btnDelete: 'Delete'\n  },"),
    ("Espagnol",
     "    calendarTitle: 'Calendario', viewDay: 'Día', viewWeek: 'Semana', viewMonth: 'Mes', today: 'Hoy', lessonsCount: 'clases'\n  },",
     "    calendarTitle: 'Calendario', viewDay: 'Día', viewWeek: 'Semana', viewMonth: 'Mes', today: 'Hoy', lessonsCount: 'clases',\n    modalEditTitle: 'Editar reserva', highSeason: 'Temporada alta', lowSeason: 'Temporada baja',\n    engHeure: 'Hora', engDemiJournee: 'Media jornada', engJournee: 'Día completo',\n    crenMatin: 'Mañana', crenApresMidi: 'Tarde',\n    fPrenom: 'Nombre', fNom: 'Apellido', fTelephone: 'Teléfono', fEmail: 'Correo electrónico', fNationalite: 'Nacionalidad',\n    fLangueParlee: 'Idioma hablado', fAge: 'Edad', fNiveau: 'Nivel', fDiscipline: 'Disciplina',\n    fNbPersonnes: 'Número de personas', fStation: 'Estación', fPointRdv: 'Punto de encuentro',\n    fDate: 'Fecha', fHeureDebut: 'Hora de inicio', fHeureFin: 'Hora de fin', fDuree: 'Duración', fPrix: 'Precio',\n    suggestedRate: 'Tarifa sugerida', fStatut: 'Estado', fModePaiement: 'Método de pago',\n    fStatutPaiement: 'Estado del pago', fNotes: 'Notas privadas',\n    btnCancel: 'Cancelar', btnSave: 'Guardar', btnCreateReservation: 'Crear reserva', btnDelete: 'Eliminar'\n  },"),
    ("Italien",
     "    calendarTitle: 'Calendario', viewDay: 'Giorno', viewWeek: 'Settimana', viewMonth: 'Mese', today: 'Oggi', lessonsCount: 'lezioni'\n  },",
     "    calendarTitle: 'Calendario', viewDay: 'Giorno', viewWeek: 'Settimana', viewMonth: 'Mese', today: 'Oggi', lessonsCount: 'lezioni',\n    modalEditTitle: 'Modifica prenotazione', highSeason: 'Alta stagione', lowSeason: 'Bassa stagione',\n    engHeure: 'Ora', engDemiJournee: 'Mezza giornata', engJournee: 'Giornata intera',\n    crenMatin: 'Mattina', crenApresMidi: 'Pomeriggio',\n    fPrenom: 'Nome', fNom: 'Cognome', fTelephone: 'Telefono', fEmail: 'E-mail', fNationalite: 'Nazionalità',\n    fLangueParlee: 'Lingua parlata', fAge: 'Età', fNiveau: 'Livello', fDiscipline: 'Disciplina',\n    fNbPersonnes: 'Numero di persone', fStation: 'Stazione', fPointRdv: \"Punto d'incontro\",\n    fDate: 'Data', fHeureDebut: 'Ora di inizio', fHeureFin: 'Ora di fine', fDuree: 'Durata', fPrix: 'Prezzo',\n    suggestedRate: 'Tariffa consigliata', fStatut: 'Stato', fModePaiement: 'Metodo di pagamento',\n    fStatutPaiement: 'Stato del pagamento', fNotes: 'Note private',\n    btnCancel: 'Annulla', btnSave: 'Salva', btnCreateReservation: 'Crea prenotazione', btnDelete: 'Elimina'\n  },"),
    ("Portugais",
     "    calendarTitle: 'Calendário', viewDay: 'Dia', viewWeek: 'Semana', viewMonth: 'Mês', today: 'Hoje', lessonsCount: 'aulas'\n  }\n};",
     "    calendarTitle: 'Calendário', viewDay: 'Dia', viewWeek: 'Semana', viewMonth: 'Mês', today: 'Hoje', lessonsCount: 'aulas',\n    modalEditTitle: 'Editar reserva', highSeason: 'Época alta', lowSeason: 'Época baixa',\n    engHeure: 'Hora', engDemiJournee: 'Meio-dia', engJournee: 'Dia inteiro',\n    crenMatin: 'Manhã', crenApresMidi: 'Tarde',\n    fPrenom: 'Nome', fNom: 'Sobrenome', fTelephone: 'Telefone', fEmail: 'E-mail', fNationalite: 'Nacionalidade',\n    fLangueParlee: 'Idioma falado', fAge: 'Idade', fNiveau: 'Nível', fDiscipline: 'Modalidade',\n    fNbPersonnes: 'Número de pessoas', fStation: 'Estação', fPointRdv: 'Ponto de encontro',\n    fDate: 'Data', fHeureDebut: 'Hora de início', fHeureFin: 'Hora de término', fDuree: 'Duração', fPrix: 'Preço',\n    suggestedRate: 'Tarifa sugerida', fStatut: 'Estado', fModePaiement: 'Método de pagamento',\n    fStatutPaiement: 'Estado do pagamento', fNotes: 'Notas privadas',\n    btnCancel: 'Cancelar', btnSave: 'Salvar', btnCreateReservation: 'Criar reserva', btnDelete: 'Excluir'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cles formulaire ajoutees pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

# Reecrire ReservationModal en entier
old_modal = """function ReservationModal({ initial, onSave, onDelete, onClose, C, settings }) {
  const [form, setForm] = useState({ type: 'Heure', creneau: 'Matin', ...initial });
  const isEdit = !!initial.id;
  const duration = useMemo(() => { const d = timeToMinutes(form.heureFin) - timeToMinutes(form.heureDebut); return d > 0 ? minutesLabel(d) : '—'; }, [form.heureDebut, form.heureFin]);
  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }));
  const CRENEAUX = getCreneaux(settings);

  const priceForType = useCallback((type, creneau, dateKey) => {
    const high = isHighSeason(dateKey, settings);
    if (type === 'Journée') return high ? settings.tarifJourneeHaute : settings.tarifJourneeBasse;
    if (type === 'Demi-journée') return high ? settings.tarifDemiJourneeHaute : settings.tarifDemiJourneeBasse;
    return null;
  }, [settings]);

  const setEngagement = (e) => {
    const type = e.target.value;
    setForm(f => {
      if (type === 'Journée') return { ...f, type, heureDebut: JOURNEE_HOURS[0], heureFin: JOURNEE_HOURS[1], prix: priceForType(type, f.creneau, f.date) };
      if (type === 'Demi-journée') { const cren = f.creneau || 'Matin'; return { ...f, type, creneau: cren, heureDebut: CRENEAUX[cren][0], heureFin: CRENEAUX[cren][1], prix: priceForType(type, cren, f.date) }; }
      return { ...f, type };
    });
  };
  const setCreneau = (e) => {
    const cren = e.target.value;
    setForm(f => ({ ...f, creneau: cren, heureDebut: CRENEAUX[cren][0], heureFin: CRENEAUX[cren][1], prix: priceForType('Demi-journée', cren, f.date) }));
  };
  const setDate = (e) => {
    const date = e.target.value;
    setForm(f => ({ ...f, date, prix: f.type !== 'Heure' ? priceForType(f.type, f.creneau, date) : f.prix }));
  };

  const high = isHighSeason(form.date, settings);
  const hourlyHint = form.type === 'Heure' ? (form.discipline === 'Ski' ? (high ? settings.tarifSkiHaute : settings.tarifSkiBasse) : (high ? settings.tarifSnowboardHaute : settings.tarifSnowboardBasse)) : null;

  const inputStyle = { border: `1px solid ${C.iceLine}`, borderRadius: 8, padding: '8px 10px', fontSize: 14, fontFamily: 'Inter, sans-serif', color: C.ink, background: C.card };
  const disabledStyle = { ...inputStyle, background: C.snowDim, color: C.inkSoft };
  const field = (label, input) => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}>
      <label style={{ fontSize: 12, fontWeight: 600, color: C.inkSoft }}>{label}</label>
      {input}
    </div>
  );

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(10,18,27,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100, padding: 20 }} onClick={onClose}>
      <div style={{ background: C.snow, borderRadius: 18, width: '100%', maxWidth: 640, maxHeight: '88vh', overflowY: 'auto', boxShadow: '0 30px 80px -30px rgba(0,0,0,0.5)' }} onClick={e => e.stopPropagation()}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '18px 24px', borderBottom: `1px solid ${C.iceLine}`, position: 'sticky', top: 0, background: C.snow, zIndex: 1 }}>
          <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 17, color: C.navy }}>{isEdit ? 'Modifier la réservation' : 'Nouvelle réservation'}</div>
          <button onClick={onClose} style={{ background: 'none', border: 'none', cursor: 'pointer', color: C.inkSoft }}><X size={20} /></button>
        </div>
        <div style={{ padding: 24, display: 'flex', flexDirection: 'column', gap: 18 }}>
          <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
            {ENGAGEMENTS.map(type => (
              <button key={type} type="button" onClick={() => setEngagement({ target: { value: type } })} style={{
                flex: 1, padding: '10px 8px', borderRadius: 9, cursor: 'pointer', fontSize: 13.5, fontWeight: 600,
                border: `1px solid ${form.type === type ? ACCENTS.glacier : C.iceLine}`,
                background: form.type === type ? ACCENTS.glacier + '18' : C.card,
                color: form.type === type ? ACCENTS.glacierDeep : C.ink
              }}>{type}</button>
            ))}
          </div>
          <Pill color={high ? ACCENTS.red : ACCENTS.green}>{high ? 'Haute saison' : 'Basse saison'}</Pill>
          {form.type === 'Demi-journée' && (
            <div style={{ display: 'flex', gap: 8 }}>
              {Object.keys(CRENEAUX).map(cren => (
                <button key={cren} type="button" onClick={() => setCreneau({ target: { value: cren } })} style={{
                  flex: 1, padding: '8px', borderRadius: 8, cursor: 'pointer', fontSize: 13, fontWeight: 600,
                  border: `1px solid ${form.creneau === cren ? ACCENTS.glacier : C.iceLine}`,
                  background: form.creneau === cren ? ACCENTS.glacier + '18' : C.card,
                  color: form.creneau === cren ? ACCENTS.glacierDeep : C.ink
                }}>{cren} ({CRENEAUX[cren][0]}–{CRENEAUX[cren][1]})</button>
              ))}
            </div>
          )}
          <div className="form-grid-2">
            {field('Prénom', <input style={inputStyle} value={form.prenom} onChange={set('prenom')} />)}
            {field('Nom', <input style={inputStyle} value={form.nom} onChange={set('nom')} />)}
            {field('Téléphone', <input style={inputStyle} value={form.telephone} onChange={set('telephone')} />)}
            {field('E-mail', <input style={inputStyle} value={form.email} onChange={set('email')} />)}
            {field('Nationalité', <input style={inputStyle} value={form.nationalite} onChange={set('nationalite')} />)}
            {field('Langue parlée', <select style={inputStyle} value={form.langue} onChange={set('langue')}>{LANGUES.map(l => <option key={l}>{l}</option>)}</select>)}
            {field('Âge', <input type="number" style={inputStyle} value={form.age} onChange={set('age')} />)}
            {field('Niveau', <select style={inputStyle} value={form.niveau} onChange={set('niveau')}>{NIVEAUX.map(n => <option key={n}>{n}</option>)}</select>)}
            {field('Discipline', <select style={inputStyle} value={form.discipline} onChange={set('discipline')}>{DISCIPLINES.map(d => <option key={d}>{d}</option>)}</select>)}
            {field('Nombre de personnes', <input type="number" min="1" style={inputStyle} value={form.nbPersonnes} onChange={set('nbPersonnes')} />)}
            {field('Station', <select style={inputStyle} value={form.station} onChange={set('station')}>{Object.entries(STATIONS_BY_MASSIF).map(([massif, list]) => <optgroup key={massif} label={massif}>{list.map(s => <option key={s}>{s}</option>)}</optgroup>)}</select>)}
            {field('Point de rendez-vous', <input style={inputStyle} value={form.pointRdv} onChange={set('pointRdv')} />)}
            {field('Date', <input type="date" style={inputStyle} value={form.date} onChange={setDate} />)}
            {field('Heure de début', <input type="time" disabled={form.type !== 'Heure'} style={form.type !== 'Heure' ? disabledStyle : inputStyle} value={form.heureDebut} onChange={set('heureDebut')} />)}
            {field('Heure de fin', <input type="time" disabled={form.type !== 'Heure'} style={form.type !== 'Heure' ? disabledStyle : inputStyle} value={form.heureFin} onChange={set('heureFin')} />)}
            {field('Durée', <div style={{ ...inputStyle, background: C.snowDim, color: C.inkSoft }}>{duration}</div>)}
            {field('Prix (€)', <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
              <input type="number" style={inputStyle} value={form.prix} onChange={set('prix')} />
              {hourlyHint && <span style={{ fontSize: 11.5, color: C.inkSoft }}>Tarif suggéré : {hourlyHint} {settings.devise || '€'}/h ({high ? 'haute' : 'basse'} saison)</span>}
            </div>)}
            {field('Statut', <select style={inputStyle} value={form.statut} onChange={set('statut')}>{STATUTS.map(s => <option key={s}>{s}</option>)}</select>)}
            {field('Mode de règlement', <select style={inputStyle} value={form.modePaiement || 'Non renseigné'} onChange={e => { const modePaiement = e.target.value; setForm(f => ({ ...f, modePaiement, paiement: modePaiement === 'Non renseigné' ? 'Non payé' : 'Payé' })); }}>{MODES_PAIEMENT.map(s => <option key={s}>{s}</option>)}</select>)}
            {field('Statut du paiement', <div style={{ ...inputStyle, background: C.snowDim, color: form.paiement === 'Payé' ? ACCENTS.green : C.inkSoft, fontWeight: 600 }}>{form.paiement}</div>)}
          </div>
          {field('Notes privées', <textarea style={{ ...inputStyle, minHeight: 70, resize: 'vertical' }} value={form.notes} onChange={set('notes')} />)}
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', padding: '16px 24px', borderTop: `1px solid ${C.iceLine}` }}>
          <div>{isEdit && <button onClick={() => onDelete(form.id)} style={{ display: 'flex', alignItems: 'center', gap: 6, background: 'none', border: 'none', color: ACCENTS.red, cursor: 'pointer', fontSize: 14, fontWeight: 600 }}><Trash2 size={15} /> Supprimer</button>}</div>
          <div style={{ display: 'flex', gap: 10 }}>
            <button onClick={onClose} style={{ padding: '9px 18px', borderRadius: 9, border: `1px solid ${C.iceLine}`, background: C.card, color: C.ink, cursor: 'pointer', fontSize: 14, fontWeight: 600 }}>Annuler</button>
            <button onClick={() => onSave(form)} style={{ padding: '9px 18px', borderRadius: 9, border: 'none', background: ACCENTS.glacier, color: '#fff', cursor: 'pointer', fontSize: 14, fontWeight: 600 }}>{isEdit ? 'Enregistrer' : 'Créer la réservation'}</button>
          </div>
        </div>
      </div>
    </div>
  );
}"""

new_modal = """function ReservationModal({ initial, onSave, onDelete, onClose, C, settings }) {
  const langue = settings.langue;
  const [form, setForm] = useState({ type: 'Heure', creneau: 'Matin', ...initial });
  const isEdit = !!initial.id;
  const duration = useMemo(() => { const d = timeToMinutes(form.heureFin) - timeToMinutes(form.heureDebut); return d > 0 ? minutesLabel(d) : '—'; }, [form.heureDebut, form.heureFin]);
  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }));
  const CRENEAUX = getCreneaux(settings);

  const engagementLabel = (type) => type === 'Heure' ? tUI('engHeure', langue) : type === 'Demi-journée' ? tUI('engDemiJournee', langue) : tUI('engJournee', langue);
  const creneauLabel = (cren) => cren === 'Matin' ? tUI('crenMatin', langue) : tUI('crenApresMidi', langue);

  const priceForType = useCallback((type, creneau, dateKey) => {
    const high = isHighSeason(dateKey, settings);
    if (type === 'Journée') return high ? settings.tarifJourneeHaute : settings.tarifJourneeBasse;
    if (type === 'Demi-journée') return high ? settings.tarifDemiJourneeHaute : settings.tarifDemiJourneeBasse;
    return null;
  }, [settings]);

  const setEngagement = (e) => {
    const type = e.target.value;
    setForm(f => {
      if (type === 'Journée') return { ...f, type, heureDebut: JOURNEE_HOURS[0], heureFin: JOURNEE_HOURS[1], prix: priceForType(type, f.creneau, f.date) };
      if (type === 'Demi-journée') { const cren = f.creneau || 'Matin'; return { ...f, type, creneau: cren, heureDebut: CRENEAUX[cren][0], heureFin: CRENEAUX[cren][1], prix: priceForType(type, cren, f.date) }; }
      return { ...f, type };
    });
  };
  const setCreneau = (e) => {
    const cren = e.target.value;
    setForm(f => ({ ...f, creneau: cren, heureDebut: CRENEAUX[cren][0], heureFin: CRENEAUX[cren][1], prix: priceForType('Demi-journée', cren, f.date) }));
  };
  const setDate = (e) => {
    const date = e.target.value;
    setForm(f => ({ ...f, date, prix: f.type !== 'Heure' ? priceForType(f.type, f.creneau, date) : f.prix }));
  };

  const high = isHighSeason(form.date, settings);
  const hourlyHint = form.type === 'Heure' ? (form.discipline === 'Ski' ? (high ? settings.tarifSkiHaute : settings.tarifSkiBasse) : (high ? settings.tarifSnowboardHaute : settings.tarifSnowboardBasse)) : null;

  const inputStyle = { border: `1px solid ${C.iceLine}`, borderRadius: 8, padding: '8px 10px', fontSize: 14, fontFamily: 'Inter, sans-serif', color: C.ink, background: C.card };
  const disabledStyle = { ...inputStyle, background: C.snowDim, color: C.inkSoft };
  const field = (label, input) => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}>
      <label style={{ fontSize: 12, fontWeight: 600, color: C.inkSoft }}>{label}</label>
      {input}
    </div>
  );

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(10,18,27,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100, padding: 20 }} onClick={onClose}>
      <div style={{ background: C.snow, borderRadius: 18, width: '100%', maxWidth: 640, maxHeight: '88vh', overflowY: 'auto', boxShadow: '0 30px 80px -30px rgba(0,0,0,0.5)' }} onClick={e => e.stopPropagation()}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '18px 24px', borderBottom: `1px solid ${C.iceLine}`, position: 'sticky', top: 0, background: C.snow, zIndex: 1 }}>
          <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 17, color: C.navy }}>{isEdit ? tUI('modalEditTitle', langue) : tUI('newReservation', langue)}</div>
          <button onClick={onClose} style={{ background: 'none', border: 'none', cursor: 'pointer', color: C.inkSoft }}><X size={20} /></button>
        </div>
        <div style={{ padding: 24, display: 'flex', flexDirection: 'column', gap: 18 }}>
          <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
            {ENGAGEMENTS.map(type => (
              <button key={type} type="button" onClick={() => setEngagement({ target: { value: type } })} style={{
                flex: 1, padding: '10px 8px', borderRadius: 9, cursor: 'pointer', fontSize: 13.5, fontWeight: 600,
                border: `1px solid ${form.type === type ? ACCENTS.glacier : C.iceLine}`,
                background: form.type === type ? ACCENTS.glacier + '18' : C.card,
                color: form.type === type ? ACCENTS.glacierDeep : C.ink
              }}>{engagementLabel(type)}</button>
            ))}
          </div>
          <Pill color={high ? ACCENTS.red : ACCENTS.green}>{high ? tUI('highSeason', langue) : tUI('lowSeason', langue)}</Pill>
          {form.type === 'Demi-journée' && (
            <div style={{ display: 'flex', gap: 8 }}>
              {Object.keys(CRENEAUX).map(cren => (
                <button key={cren} type="button" onClick={() => setCreneau({ target: { value: cren } })} style={{
                  flex: 1, padding: '8px', borderRadius: 8, cursor: 'pointer', fontSize: 13, fontWeight: 600,
                  border: `1px solid ${form.creneau === cren ? ACCENTS.glacier : C.iceLine}`,
                  background: form.creneau === cren ? ACCENTS.glacier + '18' : C.card,
                  color: form.creneau === cren ? ACCENTS.glacierDeep : C.ink
                }}>{creneauLabel(cren)} ({CRENEAUX[cren][0]}–{CRENEAUX[cren][1]})</button>
              ))}
            </div>
          )}
          <div className="form-grid-2">
            {field(tUI('fPrenom', langue), <input style={inputStyle} value={form.prenom} onChange={set('prenom')} />)}
            {field(tUI('fNom', langue), <input style={inputStyle} value={form.nom} onChange={set('nom')} />)}
            {field(tUI('fTelephone', langue), <input style={inputStyle} value={form.telephone} onChange={set('telephone')} />)}
            {field(tUI('fEmail', langue), <input style={inputStyle} value={form.email} onChange={set('email')} />)}
            {field(tUI('fNationalite', langue), <input style={inputStyle} value={form.nationalite} onChange={set('nationalite')} />)}
            {field(tUI('fLangueParlee', langue), <select style={inputStyle} value={form.langue} onChange={set('langue')}>{LANGUES.map(l => <option key={l}>{l}</option>)}</select>)}
            {field(tUI('fAge', langue), <input type="number" style={inputStyle} value={form.age} onChange={set('age')} />)}
            {field(tUI('fNiveau', langue), <select style={inputStyle} value={form.niveau} onChange={set('niveau')}>{NIVEAUX.map(n => <option key={n}>{n}</option>)}</select>)}
            {field(tUI('fDiscipline', langue), <select style={inputStyle} value={form.discipline} onChange={set('discipline')}>{DISCIPLINES.map(d => <option key={d}>{d}</option>)}</select>)}
            {field(tUI('fNbPersonnes', langue), <input type="number" min="1" style={inputStyle} value={form.nbPersonnes} onChange={set('nbPersonnes')} />)}
            {field(tUI('fStation', langue), <select style={inputStyle} value={form.station} onChange={set('station')}>{Object.entries(STATIONS_BY_MASSIF).map(([massif, list]) => <optgroup key={massif} label={massif}>{list.map(s => <option key={s}>{s}</option>)}</optgroup>)}</select>)}
            {field(tUI('fPointRdv', langue), <input style={inputStyle} value={form.pointRdv} onChange={set('pointRdv')} />)}
            {field(tUI('fDate', langue), <input type="date" style={inputStyle} value={form.date} onChange={setDate} />)}
            {field(tUI('fHeureDebut', langue), <input type="time" disabled={form.type !== 'Heure'} style={form.type !== 'Heure' ? disabledStyle : inputStyle} value={form.heureDebut} onChange={set('heureDebut')} />)}
            {field(tUI('fHeureFin', langue), <input type="time" disabled={form.type !== 'Heure'} style={form.type !== 'Heure' ? disabledStyle : inputStyle} value={form.heureFin} onChange={set('heureFin')} />)}
            {field(tUI('fDuree', langue), <div style={{ ...inputStyle, background: C.snowDim, color: C.inkSoft }}>{duration}</div>)}
            {field(`${tUI('fPrix', langue)} (${settings.devise === 'USD' ? '$' : settings.devise === 'GBP' ? '£' : '€'})`, <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
              <input type="number" style={inputStyle} value={form.prix} onChange={set('prix')} />
              {hourlyHint && <span style={{ fontSize: 11.5, color: C.inkSoft }}>{tUI('suggestedRate', langue)} : {hourlyHint} {settings.devise || '€'}/h ({high ? tUI('highSeason', langue) : tUI('lowSeason', langue)})</span>}
            </div>)}
            {field(tUI('fStatut', langue), <select style={inputStyle} value={form.statut} onChange={set('statut')}>{STATUTS.map(s => <option key={s}>{s}</option>)}</select>)}
            {field(tUI('fModePaiement', langue), <select style={inputStyle} value={form.modePaiement || 'Non renseigné'} onChange={e => { const modePaiement = e.target.value; setForm(f => ({ ...f, modePaiement, paiement: modePaiement === 'Non renseigné' ? 'Non payé' : 'Payé' })); }}>{MODES_PAIEMENT.map(s => <option key={s}>{s}</option>)}</select>)}
            {field(tUI('fStatutPaiement', langue), <div style={{ ...inputStyle, background: C.snowDim, color: form.paiement === 'Payé' ? ACCENTS.green : C.inkSoft, fontWeight: 600 }}>{form.paiement}</div>)}
          </div>
          {field(tUI('fNotes', langue), <textarea style={{ ...inputStyle, minHeight: 70, resize: 'vertical' }} value={form.notes} onChange={set('notes')} />)}
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', padding: '16px 24px', borderTop: `1px solid ${C.iceLine}` }}>
          <div>{isEdit && <button onClick={() => onDelete(form.id)} style={{ display: 'flex', alignItems: 'center', gap: 6, background: 'none', border: 'none', color: ACCENTS.red, cursor: 'pointer', fontSize: 14, fontWeight: 600 }}><Trash2 size={15} /> {tUI('btnDelete', langue)}</button>}</div>
          <div style={{ display: 'flex', gap: 10 }}>
            <button onClick={onClose} style={{ padding: '9px 18px', borderRadius: 9, border: `1px solid ${C.iceLine}`, background: C.card, color: C.ink, cursor: 'pointer', fontSize: 14, fontWeight: 600 }}>{tUI('btnCancel', langue)}</button>
            <button onClick={() => onSave(form)} style={{ padding: '9px 18px', borderRadius: 9, border: 'none', background: ACCENTS.glacier, color: '#fff', cursor: 'pointer', fontSize: 14, fontWeight: 600 }}>{isEdit ? tUI('btnSave', langue) : tUI('btnCreateReservation', langue)}</button>
          </div>
        </div>
      </div>
    </div>
  );
}"""

if old_modal in content:
    content = content.replace(old_modal, new_modal, 1)
    changes += 1
    print("OK - ReservationModal traduit")
else:
    print("ERREUR - ReservationModal non trouve (verifier correspondance exacte)")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes} modifications appliquees (Etape 4/N - Formulaire de reservation).")
