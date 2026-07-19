with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

lang_anchors = [
    ("Français",
     "    noInvoicesMatch: 'Aucune facture ne correspond à votre recherche.'\n  },",
     "    noInvoicesMatch: 'Aucune facture ne correspond à votre recherche.',\n    statsSubtitle: \"Vue d'ensemble de votre activité\", kpiHoursTaught: 'Heures enseignées',\n    kpiLessonsGiven: 'Cours réalisés', kpiAvgRevenueHour: 'Revenu moyen / heure', kpiAvgRevenueClient: 'Revenu moyen / client',\n    kpiCancelRate: \"Taux d'annulation\", kpiRetentionRate: 'Taux de fidélisation', retentionSub: 'clients avec 2+ cours',\n    kpiTotalRevenue: 'Revenu total', chartNationalities: 'Nationalités des clients', chartTopResorts: 'Stations les plus fréquentées'\n  },"),
    ("Anglais",
     "    noInvoicesMatch: 'No invoice matches your search.'\n  },",
     "    noInvoicesMatch: 'No invoice matches your search.',\n    statsSubtitle: 'Overview of your activity', kpiHoursTaught: 'Hours taught',\n    kpiLessonsGiven: 'Lessons given', kpiAvgRevenueHour: 'Average revenue / hour', kpiAvgRevenueClient: 'Average revenue / client',\n    kpiCancelRate: 'Cancellation rate', kpiRetentionRate: 'Retention rate', retentionSub: 'clients with 2+ lessons',\n    kpiTotalRevenue: 'Total revenue', chartNationalities: 'Client nationalities', chartTopResorts: 'Most visited resorts'\n  },"),
    ("Espagnol",
     "    noInvoicesMatch: 'Ninguna factura coincide con tu búsqueda.'\n  },",
     "    noInvoicesMatch: 'Ninguna factura coincide con tu búsqueda.',\n    statsSubtitle: 'Resumen de tu actividad', kpiHoursTaught: 'Horas impartidas',\n    kpiLessonsGiven: 'Clases realizadas', kpiAvgRevenueHour: 'Ingreso medio / hora', kpiAvgRevenueClient: 'Ingreso medio / cliente',\n    kpiCancelRate: 'Tasa de cancelación', kpiRetentionRate: 'Tasa de fidelización', retentionSub: 'clientes con 2+ clases',\n    kpiTotalRevenue: 'Ingreso total', chartNationalities: 'Nacionalidades de los clientes', chartTopResorts: 'Estaciones más frecuentadas'\n  },"),
    ("Italien",
     "    noInvoicesMatch: 'Nessuna fattura corrisponde alla tua ricerca.'\n  },",
     "    noInvoicesMatch: 'Nessuna fattura corrisponde alla tua ricerca.',\n    statsSubtitle: 'Panoramica della tua attività', kpiHoursTaught: 'Ore insegnate',\n    kpiLessonsGiven: 'Lezioni svolte', kpiAvgRevenueHour: 'Ricavo medio / ora', kpiAvgRevenueClient: 'Ricavo medio / cliente',\n    kpiCancelRate: 'Tasso di cancellazione', kpiRetentionRate: 'Tasso di fidelizzazione', retentionSub: 'clienti con 2+ lezioni',\n    kpiTotalRevenue: 'Ricavo totale', chartNationalities: 'Nazionalità dei clienti', chartTopResorts: 'Stazioni più frequentate'\n  },"),
    ("Portugais",
     "    noInvoicesMatch: 'Nenhuma fatura corresponde à sua busca.'\n  }\n};",
     "    noInvoicesMatch: 'Nenhuma fatura corresponde à sua busca.',\n    statsSubtitle: 'Visão geral da sua atividade', kpiHoursTaught: 'Horas ministradas',\n    kpiLessonsGiven: 'Aulas realizadas', kpiAvgRevenueHour: 'Receita média / hora', kpiAvgRevenueClient: 'Receita média / cliente',\n    kpiCancelRate: 'Taxa de cancelamento', kpiRetentionRate: 'Taxa de fidelização', retentionSub: 'clientes com 2+ aulas',\n    kpiTotalRevenue: 'Receita total', chartNationalities: 'Nacionalidades dos clientes', chartTopResorts: 'Estações mais frequentadas'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cles stats ajoutees pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

old_sv = """function StatsView({ reservations, C, devise, subscribed }) {
  const active = reservations.filter(r => r.statut !== 'Annulée');
  const clients = aggregateClients(reservations);
  const totalHeures = active.reduce((s, r) => s + (timeToMinutes(r.heureFin) - timeToMinutes(r.heureDebut)) / 60, 0);
  const totalRevenu = active.reduce((s, r) => s + Number(r.prix || 0), 0);
  const revenuMoyenHeure = totalHeures > 0 ? totalRevenu / totalHeures : 0;
  const revenuMoyenClient = clients.length > 0 ? totalRevenu / clients.length : 0;
  const tauxAnnulation = reservations.length > 0 ? (reservations.filter(r => r.statut === 'Annulée').length / reservations.length) * 100 : 0;
  const tauxFidelisation = clients.length > 0 ? (clients.filter(c => c.nbCours > 1).length / clients.length) * 100 : 0;
  const natCount = {}; clients.forEach(c => { const n = c.nationalite || 'Non renseignée'; natCount[n] = (natCount[n] || 0) + 1; });
  const natData = Object.entries(natCount).sort((a, b) => b[1] - a[1]).slice(0, 6).map(([name, value]) => ({ name, value }));
  const stationCount = {}; active.forEach(r => { stationCount[r.station] = (stationCount[r.station] || 0) + 1; });
  const stationData = Object.entries(stationCount).sort((a, b) => b[1] - a[1]).map(([name, value]) => ({ name, value }));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
      <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>Statistiques</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>Vue d'ensemble de votre activité</p></div>
      <BlurGate subscribed={subscribed} C={C}>
      <div className="kpi-grid-4">
        <KpiCard C={C} label="Heures enseignées" value={`${totalHeures.toFixed(0)}h`} icon={TrendingUp} accent={ACCENTS.blue} />
        <KpiCard C={C} label="Cours réalisés" value={active.length} icon={Repeat} accent={ACCENTS.green} />
        <KpiCard C={C} label="Clients" value={clients.length} icon={Users} accent={ACCENTS.amber} />
        <KpiCard C={C} label="Revenu moyen / heure" value={fmtEUR(revenuMoyenHeure, devise)} icon={Euro} accent={C.navy} />
      </div>
      <div className="kpi-grid-4">
        <KpiCard C={C} label="Revenu moyen / client" value={fmtEUR(revenuMoyenClient, devise)} icon={Euro} accent={ACCENTS.blue} />
        <KpiCard C={C} label="Taux d'annulation" value={`${tauxAnnulation.toFixed(0)}%`} icon={TrendingDown} accent={ACCENTS.red} />
        <KpiCard C={C} label="Taux de fidélisation" value={`${tauxFidelisation.toFixed(0)}%`} sub="clients avec 2+ cours" icon={Repeat} accent={ACCENTS.green} />
        <KpiCard C={C} label="Revenu total" value={fmtEUR(totalRevenu, devise)} icon={Euro} accent={ACCENTS.amber} />
      </div>
      <div className="two-col">
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 14 }}><Globe2 size={15} /> Nationalités des clients</div>
          <ResponsiveContainer width="100%" height={220}>
            <BarChart data={natData} layout="vertical" margin={{ left: 10 }}>
              <CartesianGrid stroke={C.ice} horizontal={false} />
              <XAxis type="number" tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={false} tickLine={false} />
              <YAxis type="category" dataKey="name" tick={{ fontSize: 12, fill: C.ink }} axisLine={false} tickLine={false} width={100} />
              <Tooltip contentStyle={{ borderRadius: 10, border: `1px solid ${C.iceLine}`, fontSize: 13 }} />
              <Bar dataKey="value" radius={[0, 6, 6, 0]} fill={ACCENTS.glacier} />
            </BarChart>
          </ResponsiveContainer>
        </div>
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 14 }}><MapPin size={15} /> Stations les plus fréquentées</div>
          <ResponsiveContainer width="100%" height={220}>
            <BarChart data={stationData}>
              <CartesianGrid stroke={C.ice} vertical={false} />
              <XAxis dataKey="name" tick={{ fontSize: 10.5, fill: C.inkSoft }} axisLine={{ stroke: C.iceLine }} tickLine={false} interval={0} angle={-20} textAnchor="end" height={50} />
              <YAxis tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={false} tickLine={false} width={30} />
              <Tooltip contentStyle={{ borderRadius: 10, border: `1px solid ${C.iceLine}`, fontSize: 13 }} />
              <Bar dataKey="value" radius={[6, 6, 0, 0]}>{stationData.map((d, i) => <Cell key={i} fill={i === 0 ? ACCENTS.amber : C.navy} />)}</Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
      </BlurGate>
    </div>
  );
}"""

new_sv = """function StatsView({ reservations, C, devise, subscribed, langue }) {
  const active = reservations.filter(r => r.statut !== 'Annulée');
  const clients = aggregateClients(reservations);
  const totalHeures = active.reduce((s, r) => s + (timeToMinutes(r.heureFin) - timeToMinutes(r.heureDebut)) / 60, 0);
  const totalRevenu = active.reduce((s, r) => s + Number(r.prix || 0), 0);
  const revenuMoyenHeure = totalHeures > 0 ? totalRevenu / totalHeures : 0;
  const revenuMoyenClient = clients.length > 0 ? totalRevenu / clients.length : 0;
  const tauxAnnulation = reservations.length > 0 ? (reservations.filter(r => r.statut === 'Annulée').length / reservations.length) * 100 : 0;
  const tauxFidelisation = clients.length > 0 ? (clients.filter(c => c.nbCours > 1).length / clients.length) * 100 : 0;
  const natCount = {}; clients.forEach(c => { const n = c.nationalite || 'Non renseignée'; natCount[n] = (natCount[n] || 0) + 1; });
  const natData = Object.entries(natCount).sort((a, b) => b[1] - a[1]).slice(0, 6).map(([name, value]) => ({ name, value }));
  const stationCount = {}; active.forEach(r => { stationCount[r.station] = (stationCount[r.station] || 0) + 1; });
  const stationData = Object.entries(stationCount).sort((a, b) => b[1] - a[1]).map(([name, value]) => ({ name, value }));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
      <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>{tUI('stats', langue)}</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>{tUI('statsSubtitle', langue)}</p></div>
      <BlurGate subscribed={subscribed} C={C}>
      <div className="kpi-grid-4">
        <KpiCard C={C} label={tUI('kpiHoursTaught', langue)} value={`${totalHeures.toFixed(0)}h`} icon={TrendingUp} accent={ACCENTS.blue} />
        <KpiCard C={C} label={tUI('kpiLessonsGiven', langue)} value={active.length} icon={Repeat} accent={ACCENTS.green} />
        <KpiCard C={C} label={tUI('clients', langue)} value={clients.length} icon={Users} accent={ACCENTS.amber} />
        <KpiCard C={C} label={tUI('kpiAvgRevenueHour', langue)} value={fmtEUR(revenuMoyenHeure, devise)} icon={Euro} accent={C.navy} />
      </div>
      <div className="kpi-grid-4">
        <KpiCard C={C} label={tUI('kpiAvgRevenueClient', langue)} value={fmtEUR(revenuMoyenClient, devise)} icon={Euro} accent={ACCENTS.blue} />
        <KpiCard C={C} label={tUI('kpiCancelRate', langue)} value={`${tauxAnnulation.toFixed(0)}%`} icon={TrendingDown} accent={ACCENTS.red} />
        <KpiCard C={C} label={tUI('kpiRetentionRate', langue)} value={`${tauxFidelisation.toFixed(0)}%`} sub={tUI('retentionSub', langue)} icon={Repeat} accent={ACCENTS.green} />
        <KpiCard C={C} label={tUI('kpiTotalRevenue', langue)} value={fmtEUR(totalRevenu, devise)} icon={Euro} accent={ACCENTS.amber} />
      </div>
      <div className="two-col">
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 14 }}><Globe2 size={15} /> {tUI('chartNationalities', langue)}</div>
          <ResponsiveContainer width="100%" height={220}>
            <BarChart data={natData} layout="vertical" margin={{ left: 10 }}>
              <CartesianGrid stroke={C.ice} horizontal={false} />
              <XAxis type="number" tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={false} tickLine={false} />
              <YAxis type="category" dataKey="name" tick={{ fontSize: 12, fill: C.ink }} axisLine={false} tickLine={false} width={100} />
              <Tooltip contentStyle={{ borderRadius: 10, border: `1px solid ${C.iceLine}`, fontSize: 13 }} />
              <Bar dataKey="value" radius={[0, 6, 6, 0]} fill={ACCENTS.glacier} />
            </BarChart>
          </ResponsiveContainer>
        </div>
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 14, fontWeight: 700, color: C.navy, marginBottom: 14 }}><MapPin size={15} /> {tUI('chartTopResorts', langue)}</div>
          <ResponsiveContainer width="100%" height={220}>
            <BarChart data={stationData}>
              <CartesianGrid stroke={C.ice} vertical={false} />
              <XAxis dataKey="name" tick={{ fontSize: 10.5, fill: C.inkSoft }} axisLine={{ stroke: C.iceLine }} tickLine={false} interval={0} angle={-20} textAnchor="end" height={50} />
              <YAxis tick={{ fontSize: 11, fill: C.inkSoft }} axisLine={false} tickLine={false} width={30} />
              <Tooltip contentStyle={{ borderRadius: 10, border: `1px solid ${C.iceLine}`, fontSize: 13 }} />
              <Bar dataKey="value" radius={[6, 6, 0, 0]}>{stationData.map((d, i) => <Cell key={i} fill={i === 0 ? ACCENTS.amber : C.navy} />)}</Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
      </BlurGate>
    </div>
  );
}"""

if old_sv in content:
    content = content.replace(old_sv, new_sv, 1)
    changes += 1
    print("OK - StatsView traduit")
else:
    print("ERREUR - StatsView non trouve")

old_call = """<StatsView reservations={reservations} C={C} devise={settings.devise} subscribed={subscribed} />"""
new_call = """<StatsView reservations={reservations} C={C} devise={settings.devise} subscribed={subscribed} langue={settings.langue} />"""

if old_call in content:
    content = content.replace(old_call, new_call, 1)
    changes += 1
    print("OK - Prop langue transmise a StatsView")
else:
    print("ERREUR - Appel StatsView non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes} modifications appliquees (Etape 8/N - Statistiques).")
