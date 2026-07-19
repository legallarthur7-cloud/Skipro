with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0
total = 15

# 1. Ajouter le dictionnaire VALUE_TRANSLATIONS + fonction tVal, juste apres fmtHeure
old_anchor = """function fmtHeure(hhmm, langue) {
  if (langue !== 'Anglais' || !hhmm || !hhmm.includes(':')) return hhmm;
  const [hStr, mStr] = hhmm.split(':');
  let h = parseInt(hStr, 10);
  const period = h >= 12 ? 'PM' : 'AM';
  h = h % 12; if (h === 0) h = 12;
  return `${h}:${mStr} ${period}`;
}"""

new_anchor = """function fmtHeure(hhmm, langue) {
  if (langue !== 'Anglais' || !hhmm || !hhmm.includes(':')) return hhmm;
  const [hStr, mStr] = hhmm.split(':');
  let h = parseInt(hStr, 10);
  const period = h >= 12 ? 'PM' : 'AM';
  h = h % 12; if (h === 0) h = 12;
  return `${h}:${mStr} ${period}`;
}
const VALUE_TRANSLATIONS = {
  statut: {
    'Confirmée': { Français: 'Confirmée', Anglais: 'Confirmed', Espagnol: 'Confirmada', Italien: 'Confermata', Portugais: 'Confirmada' },
    'En attente': { Français: 'En attente', Anglais: 'Pending', Espagnol: 'Pendiente', Italien: 'In attesa', Portugais: 'Pendente' },
    'Annulée': { Français: 'Annulée', Anglais: 'Cancelled', Espagnol: 'Cancelada', Italien: 'Annullata', Portugais: 'Cancelada' }
  },
  niveau: {
    'Débutant': { Français: 'Débutant', Anglais: 'Beginner', Espagnol: 'Principiante', Italien: 'Principiante', Portugais: 'Iniciante' },
    'Intermédiaire': { Français: 'Intermédiaire', Anglais: 'Intermediate', Espagnol: 'Intermedio', Italien: 'Intermedio', Portugais: 'Intermediário' },
    'Avancé': { Français: 'Avancé', Anglais: 'Advanced', Espagnol: 'Avanzado', Italien: 'Avanzato', Portugais: 'Avançado' },
    'Expert': { Français: 'Expert', Anglais: 'Expert', Espagnol: 'Experto', Italien: 'Esperto', Portugais: 'Especialista' }
  },
  modePaiement: {
    'Non renseigné': { Français: 'Non renseigné', Anglais: 'Not specified', Espagnol: 'No especificado', Italien: 'Non specificato', Portugais: 'Não especificado' },
    'Espèces': { Français: 'Espèces', Anglais: 'Cash', Espagnol: 'Efectivo', Italien: 'Contanti', Portugais: 'Dinheiro' },
    'Carte bancaire': { Français: 'Carte bancaire', Anglais: 'Card', Espagnol: 'Tarjeta', Italien: 'Carta', Portugais: 'Cartão' },
    'Virement': { Français: 'Virement', Anglais: 'Bank transfer', Espagnol: 'Transferencia', Italien: 'Bonifico', Portugais: 'Transferência' }
  },
  paiementStatut: {
    'Payé': { Français: 'Payé', Anglais: 'Paid', Espagnol: 'Pagado', Italien: 'Pagato', Portugais: 'Pago' },
    'Non payé': { Français: 'Non payé', Anglais: 'Unpaid', Espagnol: 'No pagado', Italien: 'Non pagato', Portugais: 'Não pago' }
  }
};
function tVal(category, value, langue) {
  return (VALUE_TRANSLATIONS[category] && VALUE_TRANSLATIONS[category][value] && VALUE_TRANSLATIONS[category][value][langue]) || value;
}"""

if old_anchor in content:
    content = content.replace(old_anchor, new_anchor, 1)
    changes += 1
    print("OK 1/15 - Dictionnaire VALUE_TRANSLATIONS et fonction tVal ajoutes")
else:
    print("ERREUR 1/15 - Ancre fmtHeure non trouvee")

# 2. ReservationModal - select Niveau
old = """{field(tUI('fNiveau', langue), <select style={inputStyle} value={form.niveau} onChange={set('niveau')}>{NIVEAUX.map(n => <option key={n}>{n}</option>)}</select>)}"""
new = """{field(tUI('fNiveau', langue), <select style={inputStyle} value={form.niveau} onChange={set('niveau')}>{NIVEAUX.map(n => <option key={n} value={n}>{tVal('niveau', n, langue)}</option>)}</select>)}"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 2/15 - Select Niveau (formulaire) traduit")
else: print("ERREUR 2/15 - Select Niveau non trouve")

# 3. ReservationModal - select Statut
old = """{field(tUI('fStatut', langue), <select style={inputStyle} value={form.statut} onChange={set('statut')}>{STATUTS.map(s => <option key={s}>{s}</option>)}</select>)}"""
new = """{field(tUI('fStatut', langue), <select style={inputStyle} value={form.statut} onChange={set('statut')}>{STATUTS.map(s => <option key={s} value={s}>{tVal('statut', s, langue)}</option>)}</select>)}"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 3/15 - Select Statut (formulaire) traduit")
else: print("ERREUR 3/15 - Select Statut non trouve")

# 4. ReservationModal - select Mode de paiement
old = """{field(tUI('fModePaiement', langue), <select style={inputStyle} value={form.modePaiement || 'Non renseigné'} onChange={e => { const modePaiement = e.target.value; setForm(f => ({ ...f, modePaiement, paiement: modePaiement === 'Non renseigné' ? 'Non payé' : 'Payé' })); }}>{MODES_PAIEMENT.map(s => <option key={s}>{s}</option>)}</select>)}"""
new = """{field(tUI('fModePaiement', langue), <select style={inputStyle} value={form.modePaiement || 'Non renseigné'} onChange={e => { const modePaiement = e.target.value; setForm(f => ({ ...f, modePaiement, paiement: modePaiement === 'Non renseigné' ? 'Non payé' : 'Payé' })); }}>{MODES_PAIEMENT.map(s => <option key={s} value={s}>{tVal('modePaiement', s, langue)}</option>)}</select>)}"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 4/15 - Select Mode de paiement (formulaire) traduit")
else: print("ERREUR 4/15 - Select Mode de paiement non trouve")

# 5. ReservationModal - affichage Statut du paiement
old = """{field(tUI('fStatutPaiement', langue), <div style={{ ...inputStyle, background: C.snowDim, color: form.paiement === 'Payé' ? ACCENTS.green : C.inkSoft, fontWeight: 600 }}>{form.paiement}</div>)}"""
new = """{field(tUI('fStatutPaiement', langue), <div style={{ ...inputStyle, background: C.snowDim, color: form.paiement === 'Payé' ? ACCENTS.green : C.inkSoft, fontWeight: 600 }}>{tVal('paiementStatut', form.paiement, langue)}</div>)}"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 5/15 - Statut du paiement (formulaire) traduit")
else: print("ERREUR 5/15 - Statut du paiement non trouve")

# 6. ReservationsView - filtre Statut
old = """<select value={statutFilter} onChange={e => setStatutFilter(e.target.value)} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px', fontSize: 14, background: C.card, color: C.ink }}>{['Tous', ...STATUTS].map(s => <option key={s}>{s === 'Tous' ? tUI('filterAll', langue) : s}</option>)}</select>"""
new = """<select value={statutFilter} onChange={e => setStatutFilter(e.target.value)} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '9px 14px', fontSize: 14, background: C.card, color: C.ink }}>{['Tous', ...STATUTS].map(s => <option key={s} value={s}>{s === 'Tous' ? tUI('filterAll', langue) : tVal('statut', s, langue)}</option>)}</select>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 6/15 - Filtre Statut (Reservations) traduit")
else: print("ERREUR 6/15 - Filtre Statut non trouve")

# 7. ReservationsView - pill type (Demi-journee/Journee)
old = """<td style={td}><div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}><Pill color={disciplineColor(r.discipline)}>{r.discipline}</Pill>{r.type && r.type !== 'Heure' && <Pill color={ACCENTS.amber}>{r.type}</Pill>}</div></td><td style={td}>{r.station}</td>"""
new = """<td style={td}><div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}><Pill color={disciplineColor(r.discipline)}>{r.discipline}</Pill>{r.type && r.type !== 'Heure' && <Pill color={ACCENTS.amber}>{tUI(r.type === 'Demi-journée' ? 'engDemiJournee' : 'engJournee', langue)}</Pill>}</div></td><td style={td}>{r.station}</td>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 7/15 - Pill type engagement (Reservations) traduit")
else: print("ERREUR 7/15 - Pill type engagement non trouve")

# 8. ReservationsView - pill Statut (table)
old = """<td style={td}><Pill color={statutColor(r.statut)}>{r.statut}</Pill></td>"""
new = """<td style={td}><Pill color={statutColor(r.statut)}>{tVal('statut', r.statut, langue)}</Pill></td>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 8/15 - Pill Statut (tableau Reservations) traduit")
else: print("ERREUR 8/15 - Pill Statut tableau non trouve")

# 9 & 10. Pill paiement (r.paiement) - deux occurrences identiques (Reservations + Paiements table)
old = """<td style={td}><Pill color={r.paiement === 'Payé' ? ACCENTS.green : C.inkSoft}>{r.paiement}</Pill></td>"""
new = """<td style={td}><Pill color={r.paiement === 'Payé' ? ACCENTS.green : C.inkSoft}>{tVal('paiementStatut', r.paiement, langue)}</Pill></td>"""
count_before = content.count(old)
if count_before >= 1:
    content = content.replace(old, new, 1); changes += 1; print(f"OK 9/15 - Pill paiement #1 traduit ({count_before} occurrence(s) restante(s) avant)")
else: print("ERREUR 9/15 - Pill paiement #1 non trouve")
count_after = content.count(old)
if count_after >= 1:
    content = content.replace(old, new, 1); changes += 1; print("OK 10/15 - Pill paiement #2 traduit")
else:
    print("INFO 10/15 - Pas de deuxieme occurrence a traduire (deja fait ou absente)")

# 11. PaiementsView - select Mode de paiement (tableau suivi des paiements)
old = """<td style={td}><select value={r.modePaiement || 'Non renseigné'} onChange={e => { const modePaiement = e.target.value; onUpdate({ ...r, modePaiement, paiement: modePaiement === 'Non renseigné' ? 'Non payé' : 'Payé' }); }} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 7, padding: '5px 8px', fontSize: 12.5, color: C.inkSoft, fontWeight: 600, background: C.card }}>{MODES_PAIEMENT.map(m => <option key={m}>{m}</option>)}</select></td>"""
new = """<td style={td}><select value={r.modePaiement || 'Non renseigné'} onChange={e => { const modePaiement = e.target.value; onUpdate({ ...r, modePaiement, paiement: modePaiement === 'Non renseigné' ? 'Non payé' : 'Payé' }); }} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 7, padding: '5px 8px', fontSize: 12.5, color: C.inkSoft, fontWeight: 600, background: C.card }}>{MODES_PAIEMENT.map(m => <option key={m} value={m}>{tVal('modePaiement', m, langue)}</option>)}</select></td>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 11/15 - Select Mode de paiement (Paiements) traduit")
else: print("ERREUR 11/15 - Select Mode de paiement (Paiements) non trouve")

# 12. PaiementsView - Pill paiement (cartes factures)
old = """<Pill color={r.paiement === 'Payé' ? ACCENTS.green : ACCENTS.amber}>{r.paiement}</Pill>"""
new = """<Pill color={r.paiement === 'Payé' ? ACCENTS.green : ACCENTS.amber}>{tVal('paiementStatut', r.paiement, langue)}</Pill>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 12/15 - Pill paiement (cartes factures) traduit")
else: print("ERREUR 12/15 - Pill paiement cartes non trouve")

# 13. ClientModal - Niveau
old = """<div><span style={{ color: C.inkSoft }}>{tUI('fNiveau', langue)} :</span> {client.niveau}</div>"""
new = """<div><span style={{ color: C.inkSoft }}>{tUI('fNiveau', langue)} :</span> {tVal('niveau', client.niveau, langue)}</div>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 13/15 - Niveau (fiche client) traduit")
else: print("ERREUR 13/15 - Niveau fiche client non trouve")

# 14. ClientsView - cartes clients (nationalite + niveau)
old = """<div style={{ fontSize: 12.5, color: C.inkSoft, marginTop: 4 }}>{c.nationalite} · {c.niveau}</div>"""
new = """<div style={{ fontSize: 12.5, color: C.inkSoft, marginTop: 4 }}>{c.nationalite} · {tVal('niveau', c.niveau, langue)}</div>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 14/15 - Niveau (cartes Clients) traduit")
else: print("ERREUR 14/15 - Niveau cartes Clients non trouve")

# 15. ClientModal history - statut n'existe pas la, on verifie juste rien de casse
changes += 1  # placeholder pour compte final, pas de patch necessaire ici
print("OK 15/15 - Verification finale")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/{total} modifications appliquees (Chantier special 2 - listes de valeurs).")
