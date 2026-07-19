with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0
total_steps = 8

# 1-5. Ajouter les nouvelles cles a chaque bloc de langue
lang_anchors = [
    ("Français", "    recentPayments: 'Derniers paiements reçus', noPaymentsRecorded: 'Aucun paiement enregistré.'\n  },",
     "    recentPayments: 'Derniers paiements reçus', noPaymentsRecorded: 'Aucun paiement enregistré.',\n    calendarTitle: 'Calendrier', viewDay: 'Jour', viewWeek: 'Semaine', viewMonth: 'Mois', today: \"Aujourd'hui\", lessonsCount: 'cours'\n  },"),
    ("Anglais", "    recentPayments: 'Recent payments', noPaymentsRecorded: 'No payments recorded.'\n  },",
     "    recentPayments: 'Recent payments', noPaymentsRecorded: 'No payments recorded.',\n    calendarTitle: 'Calendar', viewDay: 'Day', viewWeek: 'Week', viewMonth: 'Month', today: 'Today', lessonsCount: 'lessons'\n  },"),
    ("Espagnol", "    recentPayments: 'Últimos pagos recibidos', noPaymentsRecorded: 'No hay pagos registrados.'\n  },",
     "    recentPayments: 'Últimos pagos recibidos', noPaymentsRecorded: 'No hay pagos registrados.',\n    calendarTitle: 'Calendario', viewDay: 'Día', viewWeek: 'Semana', viewMonth: 'Mes', today: 'Hoy', lessonsCount: 'clases'\n  },"),
    ("Italien", "    recentPayments: 'Ultimi pagamenti ricevuti', noPaymentsRecorded: 'Nessun pagamento registrato.'\n  },",
     "    recentPayments: 'Ultimi pagamenti ricevuti', noPaymentsRecorded: 'Nessun pagamento registrato.',\n    calendarTitle: 'Calendario', viewDay: 'Giorno', viewWeek: 'Settimana', viewMonth: 'Mese', today: 'Oggi', lessonsCount: 'lezioni'\n  },"),
    ("Portugais", "    recentPayments: 'Últimos pagamentos recebidos', noPaymentsRecorded: 'Nenhum pagamento registrado.'\n  }\n};",
     "    recentPayments: 'Últimos pagamentos recebidos', noPaymentsRecorded: 'Nenhum pagamento registrado.',\n    calendarTitle: 'Calendário', viewDay: 'Dia', viewWeek: 'Semana', viewMonth: 'Mês', today: 'Hoje', lessonsCount: 'aulas'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cles calendrier ajoutees pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

# 6. Ajouter DAYS_SHORT_MAP juste apres LOCALE_MAP
old_locale = "const LOCALE_MAP = { Français: 'fr-FR', Anglais: 'en-US', Espagnol: 'es-ES', Italien: 'it-IT', Portugais: 'pt-PT' };"
new_locale = """const LOCALE_MAP = { Français: 'fr-FR', Anglais: 'en-US', Espagnol: 'es-ES', Italien: 'it-IT', Portugais: 'pt-PT' };
const DAYS_SHORT_MAP = {
  Français: ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'],
  Anglais: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  Espagnol: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'],
  Italien: ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'],
  Portugais: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
};"""

if old_locale in content:
    content = content.replace(old_locale, new_locale, 1)
    changes += 1
    print("OK 6/8 - DAYS_SHORT_MAP ajoute")
else:
    print("ERREUR 6/8 - LOCALE_MAP non trouve")

# 7. Traduire MonthGrid
old_monthgrid = """function MonthGrid({ anchor, reservations, onDayClick, C }) {
  const year = anchor.getFullYear(), month = anchor.getMonth();
  const start = startOfWeek(new Date(year, month, 1));
  const days = Array.from({ length: 42 }, (_, i) => addDays(start, i));
  const countFor = (key) => reservations.filter(r => r.date === key && r.statut !== 'Annulée').length;
  return (
    <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, overflow: 'hidden' }}>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)' }}>
        {['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'].map(d => <div key={d} style={{ textAlign: 'center', padding: '10px 0', fontSize: 11.5, fontWeight: 700, color: C.inkSoft, borderBottom: `1px solid ${C.iceLine}` }}>{d}</div>)}
        {days.map(d => {
          const key = toKey(d); const count = countFor(key); const inMonth = d.getMonth() === month;
          return (
            <div key={key} onClick={() => onDayClick(key)} style={{ minHeight: 84, borderRight: `1px solid ${C.iceLine}`, borderBottom: `1px solid ${C.iceLine}`, padding: 8, cursor: 'pointer', background: inMonth ? C.card : C.snowDim, opacity: inMonth ? 1 : 0.55 }}>
              <div style={{ fontSize: 12.5, fontWeight: key === toKey(new Date()) ? 700 : 500, color: key === toKey(new Date()) ? ACCENTS.glacier : C.ink }}>{d.getDate()}</div>
              {count > 0 && <div style={{ marginTop: 6, fontSize: 11, fontWeight: 600, color: ACCENTS.glacierDeep, background: C.ice, display: 'inline-block', padding: '2px 7px', borderRadius: 100 }}>{count} cours</div>}
            </div>
          );
        })}
      </div>
    </div>
  );
}"""

new_monthgrid = """function MonthGrid({ anchor, reservations, onDayClick, C, langue }) {
  const days_short = DAYS_SHORT_MAP[langue] || DAYS_SHORT_MAP['Français'];
  const year = anchor.getFullYear(), month = anchor.getMonth();
  const start = startOfWeek(new Date(year, month, 1));
  const days = Array.from({ length: 42 }, (_, i) => addDays(start, i));
  const countFor = (key) => reservations.filter(r => r.date === key && r.statut !== 'Annulée').length;
  return (
    <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, overflow: 'hidden' }}>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)' }}>
        {days_short.map(d => <div key={d} style={{ textAlign: 'center', padding: '10px 0', fontSize: 11.5, fontWeight: 700, color: C.inkSoft, borderBottom: `1px solid ${C.iceLine}` }}>{d}</div>)}
        {days.map(d => {
          const key = toKey(d); const count = countFor(key); const inMonth = d.getMonth() === month;
          return (
            <div key={key} onClick={() => onDayClick(key)} style={{ minHeight: 84, borderRight: `1px solid ${C.iceLine}`, borderBottom: `1px solid ${C.iceLine}`, padding: 8, cursor: 'pointer', background: inMonth ? C.card : C.snowDim, opacity: inMonth ? 1 : 0.55 }}>
              <div style={{ fontSize: 12.5, fontWeight: key === toKey(new Date()) ? 700 : 500, color: key === toKey(new Date()) ? ACCENTS.glacier : C.ink }}>{d.getDate()}</div>
              {count > 0 && <div style={{ marginTop: 6, fontSize: 11, fontWeight: 600, color: ACCENTS.glacierDeep, background: C.ice, display: 'inline-block', padding: '2px 7px', borderRadius: 100 }}>{count} {tUI('lessonsCount', langue)}</div>}
            </div>
          );
        })}
      </div>
    </div>
  );
}"""

if old_monthgrid in content:
    content = content.replace(old_monthgrid, new_monthgrid, 1)
    changes += 1
    print("OK 7/8 - MonthGrid traduit")
else:
    print("ERREUR 7/8 - MonthGrid non trouve")

# 8. Traduire CalendarView
old_calview = """function CalendarView({ reservations, onSlotClick, onEventClick, C, subscribed }) {
  const [view, setView] = useState('week');
  const [anchor, setAnchor] = useState(new Date());
  const weekStart = startOfWeek(anchor);
  const weekDays = Array.from({ length: 7 }, (_, i) => addDays(weekStart, i));
  const hours = Array.from({ length: DAY_END - DAY_START }, (_, i) => DAY_START + i);
  const byDate = useCallback((key) => reservations.filter(r => r.date === key && r.statut !== 'Annulée'), [reservations]);
  const navigate = (dir) => { if (view === 'month') setAnchor(d => { const x = new Date(d); x.setMonth(x.getMonth() + dir); return x; }); else if (view === 'week') setAnchor(d => addDays(d, dir * 7)); else setAnchor(d => addDays(d, dir)); };
  const label = view === 'month' ? anchor.toLocaleDateString('fr-FR', { month: 'long', year: 'numeric' }) : view === 'week' ? `${weekDays[0].toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' })} — ${weekDays[6].toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' })}` : anchor.toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' });"""

new_calview = """function CalendarView({ reservations, onSlotClick, onEventClick, C, subscribed, langue }) {
  const locale = LOCALE_MAP[langue] || 'fr-FR';
  const [view, setView] = useState('week');
  const [anchor, setAnchor] = useState(new Date());
  const weekStart = startOfWeek(anchor);
  const weekDays = Array.from({ length: 7 }, (_, i) => addDays(weekStart, i));
  const hours = Array.from({ length: DAY_END - DAY_START }, (_, i) => DAY_START + i);
  const byDate = useCallback((key) => reservations.filter(r => r.date === key && r.statut !== 'Annulée'), [reservations]);
  const navigate = (dir) => { if (view === 'month') setAnchor(d => { const x = new Date(d); x.setMonth(x.getMonth() + dir); return x; }); else if (view === 'week') setAnchor(d => addDays(d, dir * 7)); else setAnchor(d => addDays(d, dir)); };
  const label = view === 'month' ? anchor.toLocaleDateString(locale, { month: 'long', year: 'numeric' }) : view === 'week' ? `${weekDays[0].toLocaleDateString(locale, { day: 'numeric', month: 'short' })} — ${weekDays[6].toLocaleDateString(locale, { day: 'numeric', month: 'short' })}` : anchor.toLocaleDateString(locale, { weekday: 'long', day: 'numeric', month: 'long' });"""

if old_calview in content:
    content = content.replace(old_calview, new_calview, 1)
    changes += 1
    print("OK 8/8a - En-tete CalendarView traduit")
else:
    print("ERREUR 8/8a - En-tete CalendarView non trouve")

old_calview2 = """      <div className="header-row">
        <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>Calendrier</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4, textTransform: 'capitalize' }}>{label}</p></div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, flexWrap: 'wrap' }}>
          <div style={{ display: 'flex', border: `1px solid ${C.iceLine}`, borderRadius: 9, overflow: 'hidden' }}>
            {['day', 'week', 'month'].map(v => <button key={v} onClick={() => setView(v)} style={{ padding: '8px 14px', border: 'none', cursor: 'pointer', fontSize: 13, fontWeight: 600, background: view === v ? ACCENTS.glacier : C.card, color: view === v ? '#fff' : C.ink }}>{v === 'day' ? 'Jour' : v === 'week' ? 'Semaine' : 'Mois'}</button>)}
          </div>
          <button onClick={() => navigate(-1)} style={{ border: `1px solid ${C.iceLine}`, background: C.card, color: C.ink, borderRadius: 8, padding: 8, cursor: 'pointer' }}><ChevronLeft size={16} /></button>
          <button onClick={() => setAnchor(new Date())} style={{ border: `1px solid ${C.iceLine}`, background: C.card, color: C.ink, borderRadius: 8, padding: '8px 12px', cursor: 'pointer', fontSize: 13, fontWeight: 600 }}>Aujourd'hui</button>
          <button onClick={() => navigate(1)} style={{ border: `1px solid ${C.iceLine}`, background: C.card, color: C.ink, borderRadius: 8, padding: 8, cursor: 'pointer' }}><ChevronRight size={16} /></button>
        </div>
      </div>
      <BlurGate subscribed={subscribed} C={C}>
      {view === 'month' ? (
        <MonthGrid anchor={anchor} reservations={reservations} onDayClick={(key) => { setAnchor(new Date(key + 'T00:00:00')); setView('day'); }} C={C} />
      ) : ("""

new_calview2 = """      <div className="header-row">
        <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>{tUI('calendarTitle', langue)}</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4, textTransform: 'capitalize' }}>{label}</p></div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, flexWrap: 'wrap' }}>
          <div style={{ display: 'flex', border: `1px solid ${C.iceLine}`, borderRadius: 9, overflow: 'hidden' }}>
            {['day', 'week', 'month'].map(v => <button key={v} onClick={() => setView(v)} style={{ padding: '8px 14px', border: 'none', cursor: 'pointer', fontSize: 13, fontWeight: 600, background: view === v ? ACCENTS.glacier : C.card, color: view === v ? '#fff' : C.ink }}>{v === 'day' ? tUI('viewDay', langue) : v === 'week' ? tUI('viewWeek', langue) : tUI('viewMonth', langue)}</button>)}
          </div>
          <button onClick={() => navigate(-1)} style={{ border: `1px solid ${C.iceLine}`, background: C.card, color: C.ink, borderRadius: 8, padding: 8, cursor: 'pointer' }}><ChevronLeft size={16} /></button>
          <button onClick={() => setAnchor(new Date())} style={{ border: `1px solid ${C.iceLine}`, background: C.card, color: C.ink, borderRadius: 8, padding: '8px 12px', cursor: 'pointer', fontSize: 13, fontWeight: 600 }}>{tUI('today', langue)}</button>
          <button onClick={() => navigate(1)} style={{ border: `1px solid ${C.iceLine}`, background: C.card, color: C.ink, borderRadius: 8, padding: 8, cursor: 'pointer' }}><ChevronRight size={16} /></button>
        </div>
      </div>
      <BlurGate subscribed={subscribed} C={C}>
      {view === 'month' ? (
        <MonthGrid anchor={anchor} reservations={reservations} onDayClick={(key) => { setAnchor(new Date(key + 'T00:00:00')); setView('day'); }} C={C} langue={langue} />
      ) : ("""

if old_calview2 in content:
    content = content.replace(old_calview2, new_calview2, 1)
    changes += 1
    print("OK 8/8b - Boutons vue et bouton Aujourd'hui traduits")
else:
    print("ERREUR 8/8b - Bloc boutons non trouve")

old_calview3 = """                  <div style={{ fontSize: 11.5, color: C.inkSoft, textTransform: 'uppercase', fontWeight: 600 }}>{d.toLocaleDateString('fr-FR', { weekday: 'short' })}</div>"""
new_calview3 = """                  <div style={{ fontSize: 11.5, color: C.inkSoft, textTransform: 'uppercase', fontWeight: 600 }}>{d.toLocaleDateString(locale, { weekday: 'short' })}</div>"""

if old_calview3 in content:
    content = content.replace(old_calview3, new_calview3, 1)
    changes += 1
    print("OK 8/8c - En-tete jours colonne traduit")
else:
    print("ERREUR 8/8c - En-tete jours colonne non trouve")

# Passer la langue au CalendarView depuis App()
old_call = """<CalendarView reservations={reservations} onSlotClick={openNew} onEventClick={openEdit} C={C} subscribed={subscribed} />"""
new_call = """<CalendarView reservations={reservations} onSlotClick={openNew} onEventClick={openEdit} C={C} subscribed={subscribed} langue={settings.langue} />"""

if old_call in content:
    content = content.replace(old_call, new_call, 1)
    changes += 1
    print("OK 8/8d - Prop langue transmise a CalendarView")
else:
    print("ERREUR 8/8d - Appel CalendarView non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes} modifications appliquees (Etape 3/N - Calendrier).")
