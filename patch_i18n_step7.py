with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

lang_anchors = [
    ("Français",
     "    noClientsMatch: 'Aucun client ne correspond à votre recherche.'\n  },",
     "    noClientsMatch: 'Aucun client ne correspond à votre recherche.',\n    paymentsSubtitle: 'Suivi des encaissements, export comptable et factures clients', exportCsv: 'Exporter (CSV)',\n    kpiCollected: 'Encaissé', kpiPending: 'En attente', kpiTotalBilled: 'Total facturé',\n    tabPaymentsTracking: 'Suivi des paiements', tabInvoices: 'Factures',\n    thMontant: 'Montant', thMode: 'Mode', btnInvoice: 'Facture', btnConfirm: 'Confirmer',\n    deleteThisInvoice: 'Supprimer cette facture', searchClientInvoice: 'Rechercher un client, un n° de facture...',\n    noInvoicesMatch: 'Aucune facture ne correspond à votre recherche.'\n  },"),
    ("Anglais",
     "    noClientsMatch: 'No client matches your search.'\n  },",
     "    noClientsMatch: 'No client matches your search.',\n    paymentsSubtitle: 'Track payments, accounting export and client invoices', exportCsv: 'Export (CSV)',\n    kpiCollected: 'Collected', kpiPending: 'Pending', kpiTotalBilled: 'Total billed',\n    tabPaymentsTracking: 'Payment tracking', tabInvoices: 'Invoices',\n    thMontant: 'Amount', thMode: 'Method', btnInvoice: 'Invoice', btnConfirm: 'Confirm',\n    deleteThisInvoice: 'Delete this invoice', searchClientInvoice: 'Search a client, an invoice number...',\n    noInvoicesMatch: 'No invoice matches your search.'\n  },"),
    ("Espagnol",
     "    noClientsMatch: 'Ningún cliente coincide con tu búsqueda.'\n  },",
     "    noClientsMatch: 'Ningún cliente coincide con tu búsqueda.',\n    paymentsSubtitle: 'Seguimiento de cobros, exportación contable y facturas de clientes', exportCsv: 'Exportar (CSV)',\n    kpiCollected: 'Cobrado', kpiPending: 'Pendiente', kpiTotalBilled: 'Total facturado',\n    tabPaymentsTracking: 'Seguimiento de pagos', tabInvoices: 'Facturas',\n    thMontant: 'Importe', thMode: 'Método', btnInvoice: 'Factura', btnConfirm: 'Confirmar',\n    deleteThisInvoice: 'Eliminar esta factura', searchClientInvoice: 'Buscar un cliente, un número de factura...',\n    noInvoicesMatch: 'Ninguna factura coincide con tu búsqueda.'\n  },"),
    ("Italien",
     "    noClientsMatch: 'Nessun cliente corrisponde alla tua ricerca.'\n  },",
     "    noClientsMatch: 'Nessun cliente corrisponde alla tua ricerca.',\n    paymentsSubtitle: 'Monitoraggio incassi, esportazione contabile e fatture clienti', exportCsv: 'Esporta (CSV)',\n    kpiCollected: 'Incassato', kpiPending: 'In sospeso', kpiTotalBilled: 'Totale fatturato',\n    tabPaymentsTracking: 'Monitoraggio pagamenti', tabInvoices: 'Fatture',\n    thMontant: 'Importo', thMode: 'Metodo', btnInvoice: 'Fattura', btnConfirm: 'Conferma',\n    deleteThisInvoice: 'Elimina questa fattura', searchClientInvoice: 'Cerca un cliente, un numero di fattura...',\n    noInvoicesMatch: 'Nessuna fattura corrisponde alla tua ricerca.'\n  },"),
    ("Portugais",
     "    noClientsMatch: 'Nenhum cliente corresponde à sua busca.'\n  }\n};",
     "    noClientsMatch: 'Nenhum cliente corresponde à sua busca.',\n    paymentsSubtitle: 'Acompanhamento de recebimentos, exportação contábil e faturas de clientes', exportCsv: 'Exportar (CSV)',\n    kpiCollected: 'Recebido', kpiPending: 'Pendente', kpiTotalBilled: 'Total faturado',\n    tabPaymentsTracking: 'Acompanhamento de pagamentos', tabInvoices: 'Faturas',\n    thMontant: 'Valor', thMode: 'Método', btnInvoice: 'Fatura', btnConfirm: 'Confirmar',\n    deleteThisInvoice: 'Excluir esta fatura', searchClientInvoice: 'Buscar um cliente, um número de fatura...',\n    noInvoicesMatch: 'Nenhuma fatura corresponde à sua busca.'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cles paiements ajoutees pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

old_pv = """function PaiementsView({ reservations, onUpdate, onDelete, C, devise, settings, subscribed }) {
  const [invoiceFor, setInvoiceFor] = useState(null);
  const [subView, setSubView] = useState('paiements'); // 'paiements' | 'factures'
  const [search, setSearch] = useState('');
  const [confirmDeleteId, setConfirmDeleteId] = useState(null);
  const sorted = [...reservations].filter(r => r.statut !== 'Annulée').sort((a, b) => b.date.localeCompare(a.date));
  const encaisse = sorted.filter(r => r.paiement === 'Payé').reduce((s, r) => s + Number(r.prix || 0), 0);
  const enAttente = sorted.filter(r => r.paiement !== 'Payé').reduce((s, r) => s + Number(r.prix || 0), 0);
  const factures = sorted.filter(r => (r.prenom + r.nom).toLowerCase().includes(search.toLowerCase()) || String(r.id).slice(-6).includes(search));
  const exportCSV = () => {
    const rows = [['Date', 'Client', 'Discipline', 'Station', 'Prix', 'Paiement', 'Mode de règlement']];
    sorted.forEach(r => rows.push([r.date, `${r.prenom} ${r.nom}`, r.discipline, r.station, r.prix, r.paiement, r.modePaiement || '']));
    const csv = rows.map(row => row.map(v => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\\n');
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' }); const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = 'skipro-paiements.csv'; document.body.appendChild(a); a.click(); document.body.removeChild(a); URL.revokeObjectURL(url);
  };
  const handleDeleteClick = (id) => {
    if (confirmDeleteId === id) { onDelete(id); setConfirmDeleteId(null); }
    else setConfirmDeleteId(id);
  };
  const th = { textAlign: 'left', fontSize: 12, fontWeight: 700, color: C.inkSoft, textTransform: 'uppercase', letterSpacing: '.03em', padding: '10px 14px', borderBottom: `1px solid ${C.iceLine}` };
  const td = { padding: '11px 14px', fontSize: 13.5, borderBottom: `1px solid ${C.iceLine}`, color: C.ink };
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
      <div className="header-row">
        <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>Paiements &amp; Factures</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>Suivi des encaissements, export comptable et factures clients</p></div>
        <button onClick={exportCSV} style={{ display: 'flex', alignItems: 'center', gap: 8, background: C.card, border: `1px solid ${C.iceLine}`, color: C.ink, borderRadius: 9, padding: '10px 16px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}><Download size={15} /> Exporter (CSV)</button>
      </div>
      <BlurGate subscribed={subscribed} C={C}>
      <div className="kpi-grid-3">
        <KpiCard C={C} label="Encaissé" value={fmtEUR(encaisse, devise)} icon={Euro} accent={ACCENTS.green} />
        <KpiCard C={C} label="En attente" value={fmtEUR(enAttente, devise)} icon={Euro} accent={ACCENTS.amber} />
        <KpiCard C={C} label="Total facturé" value={fmtEUR(encaisse + enAttente, devise)} icon={Euro} accent={C.navy} />
      </div>

      <div style={{ display: 'flex', border: `1px solid ${C.iceLine}`, borderRadius: 9, overflow: 'hidden', width: 'fit-content' }}>
        <button onClick={() => setSubView('paiements')} style={{ padding: '9px 18px', border: 'none', cursor: 'pointer', fontSize: 13.5, fontWeight: 600, background: subView === 'paiements' ? ACCENTS.glacier : C.card, color: subView === 'paiements' ? '#fff' : C.ink }}>Suivi des paiements</button>
        <button onClick={() => setSubView('factures')} style={{ display: 'flex', alignItems: 'center', gap: 7, padding: '9px 18px', border: 'none', cursor: 'pointer', fontSize: 13.5, fontWeight: 600, background: subView === 'factures' ? ACCENTS.glacier : C.card, color: subView === 'factures' ? '#fff' : C.ink }}><FileText size={14} /> Factures ({sorted.length})</button>
      </div>

      {subView === 'paiements' ? (
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, overflow: 'hidden', overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead><tr><th style={th}>Client</th><th style={th}>Date</th><th style={th}>Montant</th><th style={th}>Statut</th><th style={th}>Mode</th><th style={th}></th><th style={th}></th></tr></thead>
            <tbody>
              {sorted.map(r => (
                <tr key={r.id}>
                  <td style={td}>{r.prenom} {r.nom}</td><td style={td}>{fmtDateShort(r.date)}</td>
                  <td style={{ ...td, fontWeight: 700, fontFamily: "'Space Grotesk', sans-serif" }}>{fmtEUR(r.prix, devise)}</td>
                  <td style={td}><Pill color={r.paiement === 'Payé' ? ACCENTS.green : C.inkSoft}>{r.paiement}</Pill></td>
                  <td style={td}><select value={r.modePaiement || 'Non renseigné'} onChange={e => { const modePaiement = e.target.value; onUpdate({ ...r, modePaiement, paiement: modePaiement === 'Non renseigné' ? 'Non payé' : 'Payé' }); }} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 7, padding: '5px 8px', fontSize: 12.5, color: C.inkSoft, fontWeight: 600, background: C.card }}>{MODES_PAIEMENT.map(m => <option key={m}>{m}</option>)}</select></td>
                  <td style={{ ...td, textAlign: 'right' }}>
                    <button onClick={() => setInvoiceFor(r)} style={{ display: 'inline-flex', alignItems: 'center', gap: 6, background: ACCENTS.glacier + '15', border: 'none', color: ACCENTS.glacierDeep, cursor: 'pointer', fontSize: 12.5, fontWeight: 700, padding: '6px 12px', borderRadius: 7 }}><FileText size={13} /> Facture</button>
                  </td>
                  <td style={{ ...td, textAlign: 'right' }}>
                    {confirmDeleteId === r.id ? (
                      <div style={{ display: 'flex', gap: 6, justifyContent: 'flex-end' }}>
                        <button onClick={() => handleDeleteClick(r.id)} style={{ background: ACCENTS.red, border: 'none', color: '#fff', cursor: 'pointer', fontSize: 12, fontWeight: 700, padding: '6px 10px', borderRadius: 7 }}>Confirmer</button>
                        <button onClick={() => setConfirmDeleteId(null)} style={{ background: 'none', border: `1px solid ${C.iceLine}`, color: C.ink, cursor: 'pointer', fontSize: 12, fontWeight: 600, padding: '6px 10px', borderRadius: 7 }}>Annuler</button>
                      </div>
                    ) : (
                      <button onClick={() => handleDeleteClick(r.id)} title="Supprimer cette facture" style={{ background: 'none', border: 'none', color: C.inkSoft, cursor: 'pointer', padding: 6 }}><Trash2 size={15} /></button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          <div style={{ position: 'relative', maxWidth: 360 }}>
            <Search size={15} style={{ position: 'absolute', left: 12, top: 11, color: C.inkSoft }} />
            <input placeholder="Rechercher un client, un n° de facture..." value={search} onChange={e => setSearch(e.target.value)} style={{ width: '100%', border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px 9px 34px', fontSize: 14, background: C.card, color: C.ink }} />
          </div>
          <div className="clients-grid">
            {factures.map(r => (
              <div key={r.id} style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '18px 20px', display: 'flex', flexDirection: 'column', gap: 10 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <div>
                    <div style={{ fontSize: 11.5, color: C.inkSoft, fontWeight: 600 }}>N° {String(r.id).slice(-6)}</div>
                    <div style={{ fontSize: 15, fontWeight: 700, color: C.navy, marginTop: 2 }}>{r.prenom} {r.nom}</div>
                  </div>
                  <Pill color={r.paiement === 'Payé' ? ACCENTS.green : ACCENTS.amber}>{r.paiement}</Pill>
                </div>
                <div style={{ fontSize: 12.5, color: C.inkSoft }}>{fmtDateShort(r.date)} · {r.discipline} · {r.station}</div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 6 }}>
                  <span style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 18, color: C.navy }}>{fmtEUR(r.prix, devise)}</span>
                  <div style={{ display: 'flex', gap: 6 }}>
                    <button onClick={() => setInvoiceFor(r)} style={{ display: 'inline-flex', alignItems: 'center', gap: 6, background: ACCENTS.glacier, border: 'none', color: '#fff', cursor: 'pointer', fontSize: 12.5, fontWeight: 600, padding: '7px 13px', borderRadius: 8 }}><Printer size={13} /> Voir</button>
                    {confirmDeleteId === r.id ? (
                      <>
                        <button onClick={() => handleDeleteClick(r.id)} style={{ background: ACCENTS.red, border: 'none', color: '#fff', cursor: 'pointer', fontSize: 12, fontWeight: 700, padding: '7px 10px', borderRadius: 8 }}>Confirmer</button>
                        <button onClick={() => setConfirmDeleteId(null)} style={{ background: 'none', border: `1px solid ${C.iceLine}`, color: C.ink, cursor: 'pointer', fontSize: 12, fontWeight: 600, padding: '7px 10px', borderRadius: 8 }}>Annuler</button>
                      </>
                    ) : (
                      <button onClick={() => handleDeleteClick(r.id)} title="Supprimer cette facture" style={{ background: 'none', border: `1px solid ${C.iceLine}`, color: C.inkSoft, cursor: 'pointer', padding: '7px 9px', borderRadius: 8 }}><Trash2 size={13} /></button>
                    )}
                  </div>
                </div>
              </div>
            ))}
            {factures.length === 0 && <div style={{ color: C.inkSoft, fontSize: 14 }}>Aucune facture ne correspond à votre recherche.</div>}
          </div>
        </div>
      )}

      </BlurGate>
      {invoiceFor && <InvoiceModal reservation={invoiceFor} onClose={() => setInvoiceFor(null)} C={C} devise={devise} settings={settings} />}
    </div>
  );
}"""

new_pv = """function PaiementsView({ reservations, onUpdate, onDelete, C, devise, settings, subscribed }) {
  const langue = settings.langue;
  const [invoiceFor, setInvoiceFor] = useState(null);
  const [subView, setSubView] = useState('paiements'); // 'paiements' | 'factures'
  const [search, setSearch] = useState('');
  const [confirmDeleteId, setConfirmDeleteId] = useState(null);
  const sorted = [...reservations].filter(r => r.statut !== 'Annulée').sort((a, b) => b.date.localeCompare(a.date));
  const encaisse = sorted.filter(r => r.paiement === 'Payé').reduce((s, r) => s + Number(r.prix || 0), 0);
  const enAttente = sorted.filter(r => r.paiement !== 'Payé').reduce((s, r) => s + Number(r.prix || 0), 0);
  const factures = sorted.filter(r => (r.prenom + r.nom).toLowerCase().includes(search.toLowerCase()) || String(r.id).slice(-6).includes(search));
  const exportCSV = () => {
    const rows = [['Date', 'Client', 'Discipline', 'Station', 'Prix', 'Paiement', 'Mode de règlement']];
    sorted.forEach(r => rows.push([r.date, `${r.prenom} ${r.nom}`, r.discipline, r.station, r.prix, r.paiement, r.modePaiement || '']));
    const csv = rows.map(row => row.map(v => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\\n');
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' }); const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = 'skipro-paiements.csv'; document.body.appendChild(a); a.click(); document.body.removeChild(a); URL.revokeObjectURL(url);
  };
  const handleDeleteClick = (id) => {
    if (confirmDeleteId === id) { onDelete(id); setConfirmDeleteId(null); }
    else setConfirmDeleteId(id);
  };
  const th = { textAlign: 'left', fontSize: 12, fontWeight: 700, color: C.inkSoft, textTransform: 'uppercase', letterSpacing: '.03em', padding: '10px 14px', borderBottom: `1px solid ${C.iceLine}` };
  const td = { padding: '11px 14px', fontSize: 13.5, borderBottom: `1px solid ${C.iceLine}`, color: C.ink };
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
      <div className="header-row">
        <div><h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>{tUI('paiements', langue)}</h1><p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>{tUI('paymentsSubtitle', langue)}</p></div>
        <button onClick={exportCSV} style={{ display: 'flex', alignItems: 'center', gap: 8, background: C.card, border: `1px solid ${C.iceLine}`, color: C.ink, borderRadius: 9, padding: '10px 16px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}><Download size={15} /> {tUI('exportCsv', langue)}</button>
      </div>
      <BlurGate subscribed={subscribed} C={C}>
      <div className="kpi-grid-3">
        <KpiCard C={C} label={tUI('kpiCollected', langue)} value={fmtEUR(encaisse, devise)} icon={Euro} accent={ACCENTS.green} />
        <KpiCard C={C} label={tUI('kpiPending', langue)} value={fmtEUR(enAttente, devise)} icon={Euro} accent={ACCENTS.amber} />
        <KpiCard C={C} label={tUI('kpiTotalBilled', langue)} value={fmtEUR(encaisse + enAttente, devise)} icon={Euro} accent={C.navy} />
      </div>

      <div style={{ display: 'flex', border: `1px solid ${C.iceLine}`, borderRadius: 9, overflow: 'hidden', width: 'fit-content' }}>
        <button onClick={() => setSubView('paiements')} style={{ padding: '9px 18px', border: 'none', cursor: 'pointer', fontSize: 13.5, fontWeight: 600, background: subView === 'paiements' ? ACCENTS.glacier : C.card, color: subView === 'paiements' ? '#fff' : C.ink }}>{tUI('tabPaymentsTracking', langue)}</button>
        <button onClick={() => setSubView('factures')} style={{ display: 'flex', alignItems: 'center', gap: 7, padding: '9px 18px', border: 'none', cursor: 'pointer', fontSize: 13.5, fontWeight: 600, background: subView === 'factures' ? ACCENTS.glacier : C.card, color: subView === 'factures' ? '#fff' : C.ink }}><FileText size={14} /> {tUI('tabInvoices', langue)} ({sorted.length})</button>
      </div>

      {subView === 'paiements' ? (
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, overflow: 'hidden', overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead><tr><th style={th}>{tUI('thClient', langue)}</th><th style={th}>{tUI('fDate', langue)}</th><th style={th}>{tUI('thMontant', langue)}</th><th style={th}>{tUI('fStatut', langue)}</th><th style={th}>{tUI('thMode', langue)}</th><th style={th}></th><th style={th}></th></tr></thead>
            <tbody>
              {sorted.map(r => (
                <tr key={r.id}>
                  <td style={td}>{r.prenom} {r.nom}</td><td style={td}>{fmtDateShort(r.date)}</td>
                  <td style={{ ...td, fontWeight: 700, fontFamily: "'Space Grotesk', sans-serif" }}>{fmtEUR(r.prix, devise)}</td>
                  <td style={td}><Pill color={r.paiement === 'Payé' ? ACCENTS.green : C.inkSoft}>{r.paiement}</Pill></td>
                  <td style={td}><select value={r.modePaiement || 'Non renseigné'} onChange={e => { const modePaiement = e.target.value; onUpdate({ ...r, modePaiement, paiement: modePaiement === 'Non renseigné' ? 'Non payé' : 'Payé' }); }} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 7, padding: '5px 8px', fontSize: 12.5, color: C.inkSoft, fontWeight: 600, background: C.card }}>{MODES_PAIEMENT.map(m => <option key={m}>{m}</option>)}</select></td>
                  <td style={{ ...td, textAlign: 'right' }}>
                    <button onClick={() => setInvoiceFor(r)} style={{ display: 'inline-flex', alignItems: 'center', gap: 6, background: ACCENTS.glacier + '15', border: 'none', color: ACCENTS.glacierDeep, cursor: 'pointer', fontSize: 12.5, fontWeight: 700, padding: '6px 12px', borderRadius: 7 }}><FileText size={13} /> {tUI('btnInvoice', langue)}</button>
                  </td>
                  <td style={{ ...td, textAlign: 'right' }}>
                    {confirmDeleteId === r.id ? (
                      <div style={{ display: 'flex', gap: 6, justifyContent: 'flex-end' }}>
                        <button onClick={() => handleDeleteClick(r.id)} style={{ background: ACCENTS.red, border: 'none', color: '#fff', cursor: 'pointer', fontSize: 12, fontWeight: 700, padding: '6px 10px', borderRadius: 7 }}>{tUI('btnConfirm', langue)}</button>
                        <button onClick={() => setConfirmDeleteId(null)} style={{ background: 'none', border: `1px solid ${C.iceLine}`, color: C.ink, cursor: 'pointer', fontSize: 12, fontWeight: 600, padding: '6px 10px', borderRadius: 7 }}>{tUI('btnCancel', langue)}</button>
                      </div>
                    ) : (
                      <button onClick={() => handleDeleteClick(r.id)} title={tUI('deleteThisInvoice', langue)} style={{ background: 'none', border: 'none', color: C.inkSoft, cursor: 'pointer', padding: 6 }}><Trash2 size={15} /></button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          <div style={{ position: 'relative', maxWidth: 360 }}>
            <Search size={15} style={{ position: 'absolute', left: 12, top: 11, color: C.inkSoft }} />
            <input placeholder={tUI('searchClientInvoice', langue)} value={search} onChange={e => setSearch(e.target.value)} style={{ width: '100%', border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px 9px 34px', fontSize: 14, background: C.card, color: C.ink }} />
          </div>
          <div className="clients-grid">
            {factures.map(r => (
              <div key={r.id} style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '18px 20px', display: 'flex', flexDirection: 'column', gap: 10 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <div>
                    <div style={{ fontSize: 11.5, color: C.inkSoft, fontWeight: 600 }}>N° {String(r.id).slice(-6)}</div>
                    <div style={{ fontSize: 15, fontWeight: 700, color: C.navy, marginTop: 2 }}>{r.prenom} {r.nom}</div>
                  </div>
                  <Pill color={r.paiement === 'Payé' ? ACCENTS.green : ACCENTS.amber}>{r.paiement}</Pill>
                </div>
                <div style={{ fontSize: 12.5, color: C.inkSoft }}>{fmtDateShort(r.date)} · {r.discipline} · {r.station}</div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 6 }}>
                  <span style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 18, color: C.navy }}>{fmtEUR(r.prix, devise)}</span>
                  <div style={{ display: 'flex', gap: 6 }}>
                    <button onClick={() => setInvoiceFor(r)} style={{ display: 'inline-flex', alignItems: 'center', gap: 6, background: ACCENTS.glacier, border: 'none', color: '#fff', cursor: 'pointer', fontSize: 12.5, fontWeight: 600, padding: '7px 13px', borderRadius: 8 }}><Printer size={13} /> Voir</button>
                    {confirmDeleteId === r.id ? (
                      <>
                        <button onClick={() => handleDeleteClick(r.id)} style={{ background: ACCENTS.red, border: 'none', color: '#fff', cursor: 'pointer', fontSize: 12, fontWeight: 700, padding: '7px 10px', borderRadius: 8 }}>{tUI('btnConfirm', langue)}</button>
                        <button onClick={() => setConfirmDeleteId(null)} style={{ background: 'none', border: `1px solid ${C.iceLine}`, color: C.ink, cursor: 'pointer', fontSize: 12, fontWeight: 600, padding: '7px 10px', borderRadius: 8 }}>{tUI('btnCancel', langue)}</button>
                      </>
                    ) : (
                      <button onClick={() => handleDeleteClick(r.id)} title={tUI('deleteThisInvoice', langue)} style={{ background: 'none', border: `1px solid ${C.iceLine}`, color: C.inkSoft, cursor: 'pointer', padding: '7px 9px', borderRadius: 8 }}><Trash2 size={13} /></button>
                    )}
                  </div>
                </div>
              </div>
            ))}
            {factures.length === 0 && <div style={{ color: C.inkSoft, fontSize: 14 }}>{tUI('noInvoicesMatch', langue)}</div>}
          </div>
        </div>
      )}

      </BlurGate>
      {invoiceFor && <InvoiceModal reservation={invoiceFor} onClose={() => setInvoiceFor(null)} C={C} devise={devise} settings={settings} />}
    </div>
  );
}"""

if old_pv in content:
    content = content.replace(old_pv, new_pv, 1)
    changes += 1
    print("OK - PaiementsView traduit")
else:
    print("ERREUR - PaiementsView non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes} modifications appliquees (Etape 7/N - Paiements et Factures).")
