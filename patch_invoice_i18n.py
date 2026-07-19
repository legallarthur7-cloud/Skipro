with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0
total = 8

# 1. Ajouter les nouvelles cles + fonction invoiceLessonLine, juste apres tVal
old_anchor = """function tVal(category, value, langue) {
  return (VALUE_TRANSLATIONS[category] && VALUE_TRANSLATIONS[category][value] && VALUE_TRANSLATIONS[category][value][langue]) || value;
}"""

new_anchor = """function tVal(category, value, langue) {
  return (VALUE_TRANSLATIONS[category] && VALUE_TRANSLATIONS[category][value] && VALUE_TRANSLATIONS[category][value][langue]) || value;
}
const INVOICE_TRANSLATIONS = {
  Français: { invoiceNoLabel: 'FACTURE n°', totalTTC: 'TOTAL TTC', vatMention: 'TVA non applicable, article 293 B du CGI', paidDirectly: 'Réglé en direct', bankStatement: "Relevé d'Identité Bancaire", accountHolder: 'Titulaire du compte', bankLabel: 'Banque' },
  Anglais: { invoiceNoLabel: 'INVOICE No.', totalTTC: 'TOTAL (incl. VAT)', vatMention: 'VAT not applicable — French Tax Code, article 293 B (CGI)', paidDirectly: 'Paid directly', bankStatement: 'Bank Account Details', accountHolder: 'Account holder', bankLabel: 'Bank' },
  Espagnol: { invoiceNoLabel: 'FACTURA n.º', totalTTC: 'TOTAL (IVA incl.)', vatMention: 'IVA no aplicable — Código Tributario francés, artículo 293 B (CGI)', paidDirectly: 'Pagado directamente', bankStatement: 'Datos de la cuenta bancaria', accountHolder: 'Titular de la cuenta', bankLabel: 'Banco' },
  Italien: { invoiceNoLabel: 'FATTURA n.', totalTTC: 'TOTALE (IVA incl.)', vatMention: 'IVA non applicabile — Codice Tributario francese, articolo 293 B (CGI)', paidDirectly: 'Pagato direttamente', bankStatement: 'Dati del conto bancario', accountHolder: 'Titolare del conto', bankLabel: 'Banca' },
  Portugais: { invoiceNoLabel: 'FATURA n.º', totalTTC: 'TOTAL (IVA incl.)', vatMention: 'IVA não aplicável — Código Tributário francês, artigo 293 B (CGI)', paidDirectly: 'Pago diretamente', bankStatement: 'Dados da conta bancária', accountHolder: 'Titular da conta', bankLabel: 'Banco' }
};
function tInv(key, langue) {
  return (INVOICE_TRANSLATIONS[langue] && INVOICE_TRANSLATIONS[langue][key]) || INVOICE_TRANSLATIONS['Français'][key] || key;
}
function invoiceLessonLine(r, langue) {
  const disc = r.discipline;
  const station = r.station || '';
  const dateStr = fmtDateShort(r.date);
  const time = `${fmtHeure(r.heureDebut, langue)}–${fmtHeure(r.heureFin, langue)}`;
  switch (langue) {
    case 'Anglais': return `${disc} lesson at ${station} — ${dateStr} (${time})`;
    case 'Espagnol': return `Clase de ${disc.toLowerCase()} en ${station} — ${dateStr} (${time})`;
    case 'Italien': return `Lezione di ${disc.toLowerCase()} a ${station} — ${dateStr} (${time})`;
    case 'Portugais': return `Aula de ${disc.toLowerCase()} em ${station} — ${dateStr} (${time})`;
    default: return `Cours de ${disc.toLowerCase()} à ${station} — ${dateStr} (${time})`;
  }
}"""

if old_anchor in content:
    content = content.replace(old_anchor, new_anchor, 1)
    changes += 1
    print("OK 1/8 - Dictionnaire INVOICE_TRANSLATIONS et fonctions ajoutes")
else:
    print("ERREUR 1/8 - Ancre tVal non trouvee")

# 2. todayStr - utiliser la locale dynamique
old = """  const todayStr = new Date().toLocaleDateString('fr-FR');"""
new = """  const todayStr = new Date().toLocaleDateString(LOCALE_MAP[langue] || 'fr-FR');"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 2/8 - Locale de la date facture rendue dynamique")
else: print("ERREUR 2/8 - todayStr non trouve")

# 3. Numero de facture
old = """<div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 15, color: '#10233D' }}>INVOICE n°{invoiceNumber}</div>"""
new = """<div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 15, color: '#10233D' }}>{tInv('invoiceNoLabel', langue)}{invoiceNumber}</div>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 3/8 - Numero de facture traduit")
else: print("ERREUR 3/8 - Numero de facture non trouve")

# 4. Ligne de description du cours
old = """        <div style={{ fontSize: 13.5, marginBottom: 10 }}>
          Cours de {reservation.discipline.toLowerCase()} à {reservation.station || ''} — {fmtDateShort(reservation.date)} ({fmtHeure(reservation.heureDebut, langue)}–{fmtHeure(reservation.heureFin, langue)})
        </div>"""
new = """        <div style={{ fontSize: 13.5, marginBottom: 10 }}>
          {invoiceLessonLine(reservation, langue)}
        </div>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 4/8 - Description du cours traduite")
else: print("ERREUR 4/8 - Description du cours non trouvee")

# 5. TOTAL TTC + mention TVA
old = """          <div style={{ fontSize: 15, fontWeight: 700, color: '#10233D' }}>TOTAL TTC : {fmtEUR(reservation.prix, devise)}</div>
          <div style={{ fontSize: 12, fontStyle: 'italic', color: '#5A6B7A', marginTop: 4 }}>TVA non applicable, article 293 B du CGI</div>"""
new = """          <div style={{ fontSize: 15, fontWeight: 700, color: '#10233D' }}>{tInv('totalTTC', langue)} : {fmtEUR(reservation.prix, devise)}</div>
          <div style={{ fontSize: 12, fontStyle: 'italic', color: '#5A6B7A', marginTop: 4 }}>{tInv('vatMention', langue)}</div>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 5/8 - Total TTC et mention TVA traduits")
else: print("ERREUR 5/8 - Total TTC non trouve")

# 6. Regle en direct
old = """<div style={{ fontSize: 12.5, color: '#5A6B7A', textAlign: 'center', marginTop: 14 }}>Réglé en direct — {reservation.modePaiement}</div>"""
new = """<div style={{ fontSize: 12.5, color: '#5A6B7A', textAlign: 'center', marginTop: 14 }}>{tInv('paidDirectly', langue)} — {tVal('modePaiement', reservation.modePaiement, langue)}</div>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 6/8 - Mention 'Regle en direct' traduite")
else: print("ERREUR 6/8 - Mention Regle en direct non trouvee")

# 7. RIB - titre + titulaire
old = """<div style={{ fontWeight: 700, color: '#16232F', marginBottom: 6 }}>Relevé d'Identité Bancaire</div>
            <div>Titulaire du compte : {settings.nom}</div>"""
new = """<div style={{ fontWeight: 700, color: '#16232F', marginBottom: 6 }}>{tInv('bankStatement', langue)}</div>
            <div>{tInv('accountHolder', langue)} : {settings.nom}</div>"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 7/8 - Titre RIB et titulaire traduits")
else: print("ERREUR 7/8 - Titre RIB non trouve")

# 8. Label Banque
old = """{settings.banque && <div>Banque : {settings.banque}</div>}"""
new = """{settings.banque && <div>{tInv('bankLabel', langue)} : {settings.banque}</div>}"""
if old in content:
    content = content.replace(old, new, 1); changes += 1; print("OK 8/8 - Label Banque traduit")
else: print("ERREUR 8/8 - Label Banque non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/{total} modifications appliquees (Traduction complete de la facture).")
