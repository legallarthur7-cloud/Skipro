with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

# 1. Etendre le dictionnaire de traductions avec les cles du Dashboard
old_dict = """const UI_TRANSLATIONS = {
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
}"""

new_dict = """const UI_TRANSLATIONS = {
  Français: {
    dashboard: 'Tableau de bord', calendar: 'Calendrier', reservations: 'Réservations',
    clients: 'Clients', paiements: 'Paiements & Factures', stats: 'Statistiques',
    parametres: 'Paramètres', deconnexion: 'Déconnexion',
    newReservation: 'Nouvelle réservation',
    subscribeTitle: 'Abonne-toi pour débloquer tes statistiques',
    subscribeSub: "Rends-toi dans Paramètres pour t'abonner (29€/mois).",
    kpiTodayLessons: "Cours aujourd'hui", hoursTaught: 'enseignées',
    kpiWeekLessons: 'Cours cette semaine', kpiMonthRevenue: 'Revenus du mois',
    lessonsThisMonth: 'cours ce mois-ci', kpiFillRate: 'Taux de remplissage', thisWeek: 'cette semaine',
    kpiTodayRevenue: 'Revenus du jour', kpiSeasonRevenue: 'Revenus de la saison',
    kpiTotalClients: 'Total clients', newClientsThisMonth: 'nouveaux ce mois-ci',
    kpiSeasonHours: 'Heures — saison',
    chartRevenue14d: "Évolution du chiffre d'affaires (14 jours)", chartDisciplineSplit: 'Répartition des disciplines',
    upcomingLessons: 'Prochains cours', noUpcomingLessons: 'Aucun cours à venir.',
    recentPayments: 'Derniers paiements reçus', noPaymentsRecorded: 'Aucun paiement enregistré.'
  },
  Anglais: {
    dashboard: 'Dashboard', calendar: 'Calendar', reservations: 'Bookings',
    clients: 'Clients', paiements: 'Payments & Invoices', stats: 'Statistics',
    parametres: 'Settings', deconnexion: 'Log out',
    newReservation: 'New booking',
    subscribeTitle: 'Subscribe to unlock your stats',
    subscribeSub: 'Go to Settings to subscribe (€29/month).',
    kpiTodayLessons: 'Lessons today', hoursTaught: 'taught',
    kpiWeekLessons: 'Lessons this week', kpiMonthRevenue: 'Revenue this month',
    lessonsThisMonth: 'lessons this month', kpiFillRate: 'Fill rate', thisWeek: 'this week',
    kpiTodayRevenue: "Today's revenue", kpiSeasonRevenue: 'Season revenue',
    kpiTotalClients: 'Total clients', newClientsThisMonth: 'new this month',
    kpiSeasonHours: 'Hours — season',
    chartRevenue14d: 'Revenue trend (14 days)', chartDisciplineSplit: 'Discipline breakdown',
    upcomingLessons: 'Upcoming lessons', noUpcomingLessons: 'No upcoming lessons.',
    recentPayments: 'Recent payments', noPaymentsRecorded: 'No payments recorded.'
  },
  Espagnol: {
    dashboard: 'Panel', calendar: 'Calendario', reservations: 'Reservas',
    clients: 'Clientes', paiements: 'Pagos y Facturas', stats: 'Estadísticas',
    parametres: 'Ajustes', deconnexion: 'Cerrar sesión',
    newReservation: 'Nueva reserva',
    subscribeTitle: 'Suscríbete para desbloquear tus estadísticas',
    subscribeSub: 'Ve a Ajustes para suscribirte (29€/mes).',
    kpiTodayLessons: 'Clases hoy', hoursTaught: 'impartidas',
    kpiWeekLessons: 'Clases esta semana', kpiMonthRevenue: 'Ingresos del mes',
    lessonsThisMonth: 'clases este mes', kpiFillRate: 'Tasa de ocupación', thisWeek: 'esta semana',
    kpiTodayRevenue: 'Ingresos de hoy', kpiSeasonRevenue: 'Ingresos de la temporada',
    kpiTotalClients: 'Total de clientes', newClientsThisMonth: 'nuevos este mes',
    kpiSeasonHours: 'Horas — temporada',
    chartRevenue14d: 'Evolución de ingresos (14 días)', chartDisciplineSplit: 'Reparto por disciplina',
    upcomingLessons: 'Próximas clases', noUpcomingLessons: 'No hay clases próximas.',
    recentPayments: 'Últimos pagos recibidos', noPaymentsRecorded: 'No hay pagos registrados.'
  },
  Italien: {
    dashboard: 'Bacheca', calendar: 'Calendario', reservations: 'Prenotazioni',
    clients: 'Clienti', paiements: 'Pagamenti e Fatture', stats: 'Statistiche',
    parametres: 'Impostazioni', deconnexion: 'Disconnetti',
    newReservation: 'Nuova prenotazione',
    subscribeTitle: 'Abbonati per sbloccare le tue statistiche',
    subscribeSub: 'Vai su Impostazioni per abbonarti (29€/mese).',
    kpiTodayLessons: 'Lezioni oggi', hoursTaught: 'insegnate',
    kpiWeekLessons: 'Lezioni questa settimana', kpiMonthRevenue: 'Entrate del mese',
    lessonsThisMonth: 'lezioni questo mese', kpiFillRate: 'Tasso di riempimento', thisWeek: 'questa settimana',
    kpiTodayRevenue: 'Entrate di oggi', kpiSeasonRevenue: 'Entrate stagionali',
    kpiTotalClients: 'Totale clienti', newClientsThisMonth: 'nuovi questo mese',
    kpiSeasonHours: 'Ore — stagione',
    chartRevenue14d: 'Andamento entrate (14 giorni)', chartDisciplineSplit: 'Ripartizione discipline',
    upcomingLessons: 'Prossime lezioni', noUpcomingLessons: 'Nessuna lezione in programma.',
    recentPayments: 'Ultimi pagamenti ricevuti', noPaymentsRecorded: 'Nessun pagamento registrato.'
  },
  Portugais: {
    dashboard: 'Painel', calendar: 'Calendário', reservations: 'Reservas',
    clients: 'Clientes', paiements: 'Pagamentos e Faturas', stats: 'Estatísticas',
    parametres: 'Configurações', deconnexion: 'Sair',
    newReservation: 'Nova reserva',
    subscribeTitle: 'Assine para desbloquear suas estatísticas',
    subscribeSub: 'Vá em Configurações para assinar (29€/mês).',
    kpiTodayLessons: 'Aulas hoje', hoursTaught: 'ministradas',
    kpiWeekLessons: 'Aulas esta semana', kpiMonthRevenue: 'Receita do mês',
    lessonsThisMonth: 'aulas este mês', kpiFillRate: 'Taxa de ocupação', thisWeek: 'esta semana',
    kpiTodayRevenue: 'Receita de hoje', kpiSeasonRevenue: 'Receita da temporada',
    kpiTotalClients: 'Total de clientes', newClientsThisMonth: 'novos este mês',
    kpiSeasonHours: 'Horas — temporada',
    chartRevenue14d: 'Evolução da receita (14 dias)', chartDisciplineSplit: 'Distribuição por modalidade',
    upcomingLessons: 'Próximas aulas', noUpcomingLessons: 'Nenhuma aula agendada.',
    recentPayments: 'Últimos pagamentos recebidos', noPaymentsRecorded: 'Nenhum pagamento registrado.'
  }
};
const LOCALE_MAP = { Français: 'fr-FR', Anglais: 'en-US', Espagnol: 'es-ES', Italien: 'it-IT', Portugais: 'pt-PT' };
function tUI(key, langue) {
  return (UI_TRANSLATIONS[langue] && UI_TRANSLATIONS[langue][key]) || UI_TRANSLATIONS['Français'][key] || key;
}"""

if old_dict in content:
    content = content.replace(old_dict, new_dict, 1)
    changes += 1
    print("OK 1/3 - Dictionnaire etendu avec les cles Dashboard")
else:
    print("ERREUR 1/3 - Ancien dictionnaire non trouve")

# 2. Remplacer le composant Dashboard entier
old_dash = """function Dashboard({ reservations, onNewReservation, C, devise, subscribed }) {
  const today = new Date(); const todayKey = toKey(today); const weekStart = startOfWeek(today);
  const monthKey = `${today.getFullYear()}-${pad(today.getMonth() + 1)}`;
  const inWeek = (k) => { const d = new Date(k + 'T00:00:00'); return d >= weekStart && d < addDays(weekStart, 7); };
  const inMonth = (k) => k.startsWith(monthKey);
  const active = reservations.filter(r => r.statut !== 'Annulée');
  const todayR = active.filter(r => r.date === todayKey);
  const weekR = active.filter(r => inWeek(r.date));
  const monthR = active.filter(r => inMonth(r.date));
  const seasonR = active;
  const hoursOf = (l) => l.reduce((s, r) => s + (timeToMinutes(r.heureFin) - timeToMinutes(r.heureDebut)) / 60, 0);
  const revenueOf = (l) => l.reduce((s, r) => s + Number(r.prix || 0), 0);
  const uniqueClients = new Set(seasonR.map(r => r.prenom + r.nom)).size;
  const newClientsThisMonth = new Set(monthR.map(r => r.prenom + r.nom)).size;
  const fillRate = Math.min(100, Math.round((hoursOf(weekR) / (8 * 6)) * 100));
  const lastPayments = [...reservations].filter(r => r.paiement === 'Payé').sort((a, b) => b.date.localeCompare(a.date)).slice(0, 5);
  const upcoming = [...reservations].filter(r => r.date >= todayKey && r.statut !== 'Annulée').sort((a, b) => (a.date + a.heureDebut).localeCompare(b.date + b.heureDebut)).slice(0, 5);
  const revEvolution = [];
  for (let i = -13; i <= 0; i++) { const d = addDays(today, i); const key = toKey(d); revEvolution.push({ label: d.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' }), revenu: revenueOf(active.filter(r => r.date === key)) }); }
  const disciplineData = DISCIPLINES.map(d => ({ name: d, value: seasonR.filter(r => r.discipline === d).length }));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
      <div className="header-row">
        <div>
          <h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>Tableau de bord</h1>
          <p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>{today.toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' })}</p>
        </div>
        <button onClick={onNewReservation} style={{ display: 'flex', alignItems: 'center', gap: 8, background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '10px 18px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}><Plus size={16} /> Nouvelle réservation</button>
      </div>
      <div style={{ position: 'relative' }}>
        {!subscribed && (
          <div style={{ position: 'absolute', inset: 0, zIndex: 10, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 20 }}>
            <div style={{ background: '#fff', border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 26px', boxShadow: '0 12px 30px -10px rgba(0,0,0,0.2)', textAlign: 'center', maxWidth: 320 }}>
              <div style={{ fontWeight: 700, color: C.navy, marginBottom: 6 }}>Abonne-toi pour débloquer tes statistiques</div>
              <div style={{ fontSize: 13, color: C.inkSoft }}>Rends-toi dans Paramètres pour t'abonner (29€/mois).</div>
            </div>
          </div>
        )}
        <div className="kpi-grid-4" style={!subscribed ? { filter: 'blur(6px)', pointerEvents: 'none', userSelect: 'none' } : {}}>
          <KpiCard C={C} label="Cours aujourd'hui" value={todayR.length} sub={`${hoursOf(todayR).toFixed(1)}h enseignées`} icon={CalendarIcon} accent={ACCENTS.blue} />
          <KpiCard C={C} label="Cours cette semaine" value={weekR.length} sub={`${hoursOf(weekR).toFixed(1)}h enseignées`} icon={Clock} accent={ACCENTS.green} />
          <KpiCard C={C} label="Revenus du mois" value={fmtEUR(revenueOf(monthR), devise)} sub={`${monthR.length} cours ce mois-ci`} icon={Euro} accent={ACCENTS.amber} />
          <KpiCard C={C} label="Taux de remplissage" value={`${fillRate}%`} sub="cette semaine" icon={TrendingUp} accent={C.navy} />
        </div>
        <div className="kpi-grid-4" style={!subscribed ? { filter: 'blur(6px)', pointerEvents: 'none', userSelect: 'none', marginTop: 14 } : { marginTop: 14 }}>
          <KpiCard C={C} label="Revenus du jour" value={fmtEUR(revenueOf(todayR), devise)} icon={Euro} accent={ACCENTS.green} />
          <KpiCard C={C} label="Revenus de la saison" value={fmtEUR(revenueOf(seasonR), devise)} icon={Euro} accent={ACCENTS.blue} />
          <KpiCard C={C} label="Total clients" value={uniqueClients} sub={`${newClientsThisMonth} nouveaux ce mois-ci`} icon={Users} accent={ACCENTS.amber} />
          <KpiCard C={C} label="Heures — saison" value={`${hoursOf(seasonR).toFixed(0)}h`} icon={Clock} accent={C.navy} />
        </div>
      </div>
      <div className="chart-grid">
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px' }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 14 }}>Évolution du chiffre d'affaires (14 jours)</div>
          <ResponsiveContainer width="100%" height={220}>
            <LineChart data={revEvolution}>
              <CartesianGrid stroke={C.ice} vertical={false} />
              <XAxis dataKey="label" tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={{ stroke: C.iceLine }} tickLine={false} interval={1} />
              <YAxis tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={false} tickLine={false} width={40} />
              <Tooltip formatter={(v) => fmtEUR(v, devise)} contentStyle={{ borderRadius: 10, border: `1px solid ${C.iceLine}`, fontSize: 13 }} />
              <Line type="monotone" dataKey="revenu" stroke={ACCENTS.glacier} strokeWidth={2.5} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px' }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 14 }}>Répartition des disciplines</div>
          <ResponsiveContainer width="100%" height={220}>
            <BarChart data={disciplineData}>
              <CartesianGrid stroke={C.ice} vertical={false} />
              <XAxis dataKey="name" tick={{ fontSize: 12, fill: C.inkSoft }} axisLine={{ stroke: C.iceLine }} tickLine={false} />
              <YAxis tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={false} tickLine={false} width={30} />
              <Tooltip contentStyle={{ borderRadius: 10, border: `1px solid ${C.iceLine}`, fontSize: 13 }} />
              <Bar dataKey="value" radius={[6, 6, 0, 0]}>{disciplineData.map((d, i) => <Cell key={i} fill={disciplineColor(d.name)} />)}</Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
      <div className="two-col">
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '18px 22px' }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 12 }}>Prochains cours</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            {upcoming.length === 0 && <div style={{ fontSize: 13.5, color: C.inkSoft }}>Aucun cours à venir.</div>}
            {upcoming.map(r => (
              <div key={r.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: 10, borderBottom: `1px dashed ${C.iceLine}` }}>
                <div><div style={{ fontSize: 13.5, fontWeight: 600, color: C.ink }}>{r.prenom} {r.nom}</div><div style={{ fontSize: 12.5, color: C.inkSoft }}>{fmtDateShort(r.date)} · {r.heureDebut} · {r.station}</div></div>
                <Pill color={disciplineColor(r.discipline)}>{r.discipline}</Pill>
              </div>
            ))}
          </div>
        </div>
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '18px 22px' }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 12 }}>Derniers paiements reçus</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            {lastPayments.length === 0 && <div style={{ fontSize: 13.5, color: C.inkSoft }}>Aucun paiement enregistré.</div>}
            {lastPayments.map(r => (
              <div key={r.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: 10, borderBottom: `1px dashed ${C.iceLine}` }}>
                <div><div style={{ fontSize: 13.5, fontWeight: 600, color: C.ink }}>{r.prenom} {r.nom}</div><div style={{ fontSize: 12.5, color: C.inkSoft }}>{fmtDateShort(r.date)}</div></div>
                <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, color: ACCENTS.green }}>{fmtEUR(r.prix, devise)}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}"""

new_dash = """function Dashboard({ reservations, onNewReservation, C, devise, subscribed, langue }) {
  const locale = LOCALE_MAP[langue] || 'fr-FR';
  const tt = (key) => tUI(key, langue);
  const today = new Date(); const todayKey = toKey(today); const weekStart = startOfWeek(today);
  const monthKey = `${today.getFullYear()}-${pad(today.getMonth() + 1)}`;
  const inWeek = (k) => { const d = new Date(k + 'T00:00:00'); return d >= weekStart && d < addDays(weekStart, 7); };
  const inMonth = (k) => k.startsWith(monthKey);
  const active = reservations.filter(r => r.statut !== 'Annulée');
  const todayR = active.filter(r => r.date === todayKey);
  const weekR = active.filter(r => inWeek(r.date));
  const monthR = active.filter(r => inMonth(r.date));
  const seasonR = active;
  const hoursOf = (l) => l.reduce((s, r) => s + (timeToMinutes(r.heureFin) - timeToMinutes(r.heureDebut)) / 60, 0);
  const revenueOf = (l) => l.reduce((s, r) => s + Number(r.prix || 0), 0);
  const uniqueClients = new Set(seasonR.map(r => r.prenom + r.nom)).size;
  const newClientsThisMonthCount = new Set(monthR.map(r => r.prenom + r.nom)).size;
  const fillRate = Math.min(100, Math.round((hoursOf(weekR) / (8 * 6)) * 100));
  const lastPayments = [...reservations].filter(r => r.paiement === 'Payé').sort((a, b) => b.date.localeCompare(a.date)).slice(0, 5);
  const upcoming = [...reservations].filter(r => r.date >= todayKey && r.statut !== 'Annulée').sort((a, b) => (a.date + a.heureDebut).localeCompare(b.date + b.heureDebut)).slice(0, 5);
  const revEvolution = [];
  for (let i = -13; i <= 0; i++) { const d = addDays(today, i); const key = toKey(d); revEvolution.push({ label: d.toLocaleDateString(locale, { day: 'numeric', month: 'short' }), revenu: revenueOf(active.filter(r => r.date === key)) }); }
  const disciplineData = DISCIPLINES.map(d => ({ name: d, value: seasonR.filter(r => r.discipline === d).length }));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
      <div className="header-row">
        <div>
          <h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>{tt('dashboard')}</h1>
          <p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>{today.toLocaleDateString(locale, { weekday: 'long', day: 'numeric', month: 'long' })}</p>
        </div>
        <button onClick={onNewReservation} style={{ display: 'flex', alignItems: 'center', gap: 8, background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '10px 18px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}><Plus size={16} /> {tt('newReservation')}</button>
      </div>
      <div style={{ position: 'relative' }}>
        {!subscribed && (
          <div style={{ position: 'absolute', inset: 0, zIndex: 10, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 20 }}>
            <div style={{ background: '#fff', border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 26px', boxShadow: '0 12px 30px -10px rgba(0,0,0,0.2)', textAlign: 'center', maxWidth: 320 }}>
              <div style={{ fontWeight: 700, color: C.navy, marginBottom: 6 }}>{tt('subscribeTitle')}</div>
              <div style={{ fontSize: 13, color: C.inkSoft }}>{tt('subscribeSub')}</div>
            </div>
          </div>
        )}
        <div className="kpi-grid-4" style={!subscribed ? { filter: 'blur(6px)', pointerEvents: 'none', userSelect: 'none' } : {}}>
          <KpiCard C={C} label={tt('kpiTodayLessons')} value={todayR.length} sub={`${hoursOf(todayR).toFixed(1)}h ${tt('hoursTaught')}`} icon={CalendarIcon} accent={ACCENTS.blue} />
          <KpiCard C={C} label={tt('kpiWeekLessons')} value={weekR.length} sub={`${hoursOf(weekR).toFixed(1)}h ${tt('hoursTaught')}`} icon={Clock} accent={ACCENTS.green} />
          <KpiCard C={C} label={tt('kpiMonthRevenue')} value={fmtEUR(revenueOf(monthR), devise)} sub={`${monthR.length} ${tt('lessonsThisMonth')}`} icon={Euro} accent={ACCENTS.amber} />
          <KpiCard C={C} label={tt('kpiFillRate')} value={`${fillRate}%`} sub={tt('thisWeek')} icon={TrendingUp} accent={C.navy} />
        </div>
        <div className="kpi-grid-4" style={!subscribed ? { filter: 'blur(6px)', pointerEvents: 'none', userSelect: 'none', marginTop: 14 } : { marginTop: 14 }}>
          <KpiCard C={C} label={tt('kpiTodayRevenue')} value={fmtEUR(revenueOf(todayR), devise)} icon={Euro} accent={ACCENTS.green} />
          <KpiCard C={C} label={tt('kpiSeasonRevenue')} value={fmtEUR(revenueOf(seasonR), devise)} icon={Euro} accent={ACCENTS.blue} />
          <KpiCard C={C} label={tt('kpiTotalClients')} value={uniqueClients} sub={`${newClientsThisMonthCount} ${tt('newClientsThisMonth')}`} icon={Users} accent={ACCENTS.amber} />
          <KpiCard C={C} label={tt('kpiSeasonHours')} value={`${hoursOf(seasonR).toFixed(0)}h`} icon={Clock} accent={C.navy} />
        </div>
      </div>
      <div className="chart-grid">
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px' }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 14 }}>{tt('chartRevenue14d')}</div>
          <ResponsiveContainer width="100%" height={220}>
            <LineChart data={revEvolution}>
              <CartesianGrid stroke={C.ice} vertical={false} />
              <XAxis dataKey="label" tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={{ stroke: C.iceLine }} tickLine={false} interval={1} />
              <YAxis tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={false} tickLine={false} width={40} />
              <Tooltip formatter={(v) => fmtEUR(v, devise)} contentStyle={{ borderRadius: 10, border: `1px solid ${C.iceLine}`, fontSize: 13 }} />
              <Line type="monotone" dataKey="revenu" stroke={ACCENTS.glacier} strokeWidth={2.5} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px' }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 14 }}>{tt('chartDisciplineSplit')}</div>
          <ResponsiveContainer width="100%" height={220}>
            <BarChart data={disciplineData}>
              <CartesianGrid stroke={C.ice} vertical={false} />
              <XAxis dataKey="name" tick={{ fontSize: 12, fill: C.inkSoft }} axisLine={{ stroke: C.iceLine }} tickLine={false} />
              <YAxis tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={false} tickLine={false} width={30} />
              <Tooltip contentStyle={{ borderRadius: 10, border: `1px solid ${C.iceLine}`, fontSize: 13 }} />
              <Bar dataKey="value" radius={[6, 6, 0, 0]}>{disciplineData.map((d, i) => <Cell key={i} fill={disciplineColor(d.name)} />)}</Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
      <div className="two-col">
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '18px 22px' }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 12 }}>{tt('upcomingLessons')}</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            {upcoming.length === 0 && <div style={{ fontSize: 13.5, color: C.inkSoft }}>{tt('noUpcomingLessons')}</div>}
            {upcoming.map(r => (
              <div key={r.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: 10, borderBottom: `1px dashed ${C.iceLine}` }}>
                <div><div style={{ fontSize: 13.5, fontWeight: 600, color: C.ink }}>{r.prenom} {r.nom}</div><div style={{ fontSize: 12.5, color: C.inkSoft }}>{fmtDateShort(r.date)} · {r.heureDebut} · {r.station}</div></div>
                <Pill color={disciplineColor(r.discipline)}>{r.discipline}</Pill>
              </div>
            ))}
          </div>
        </div>
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '18px 22px' }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 12 }}>{tt('recentPayments')}</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            {lastPayments.length === 0 && <div style={{ fontSize: 13.5, color: C.inkSoft }}>{tt('noPaymentsRecorded')}</div>}
            {lastPayments.map(r => (
              <div key={r.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: 10, borderBottom: `1px dashed ${C.iceLine}` }}>
                <div><div style={{ fontSize: 13.5, fontWeight: 600, color: C.ink }}>{r.prenom} {r.nom}</div><div style={{ fontSize: 12.5, color: C.inkSoft }}>{fmtDateShort(r.date)}</div></div>
                <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, color: ACCENTS.green }}>{fmtEUR(r.prix, devise)}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}"""

if old_dash in content:
    content = content.replace(old_dash, new_dash, 1)
    changes += 1
    print("OK 2/3 - Composant Dashboard traduit")
else:
    print("ERREUR 2/3 - Composant Dashboard non trouve (verifier correspondance exacte)")

# 3. Passer la langue au composant Dashboard depuis App()
old_call = """<Dashboard reservations={reservations} onNewReservation={() => openNew()} C={C} devise={settings.devise} subscribed={subscribed} />"""
new_call = """<Dashboard reservations={reservations} onNewReservation={() => openNew()} C={C} devise={settings.devise} subscribed={subscribed} langue={settings.langue} />"""

if old_call in content:
    content = content.replace(old_call, new_call, 1)
    changes += 1
    print("OK 3/3 - Prop langue transmise au Dashboard")
else:
    print("ERREUR 3/3 - Appel Dashboard non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/3 modifications appliquees (Etape 2/N - Tableau de bord).")
