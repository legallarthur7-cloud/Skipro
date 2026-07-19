with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

# 1. Ajouter les champs bancaires + profession à DEFAULT_SETTINGS
old_settings = """const DEFAULT_SETTINGS = {
  nom: 'Moniteur ESF', email: 'contact@exemple.com', devise: 'EUR', langue: 'Français',
  fuseauHoraire: 'Europe/Paris',
  adresse: '', telephone: '', siret: '',"""

new_settings = """const DEFAULT_SETTINGS = {
  nom: 'Moniteur ESF', email: 'contact@exemple.com', devise: 'EUR', langue: 'Français',
  fuseauHoraire: 'Europe/Paris',
  adresse: '', telephone: '', siret: '', profession: 'Moniteur de ski indépendant',
  iban: '', bic: '', banque: '',"""

if old_settings in content:
    content = content.replace(old_settings, new_settings)
    changes += 1
    print("OK 1/3 - DEFAULT_SETTINGS mis a jour")
else:
    print("ERREUR 1/3 - Bloc DEFAULT_SETTINGS non trouve")

# 2. Ajouter une section "Coordonnées bancaires" après Coordonnées, avant Préférences régionales
old_coords = """      {section('Coordonnées', (
        <>
        <div className="form-grid-2">
          {field('Nom affiché', <input style={inputStyle} value={form.nom} onChange={set('nom')} />)}
          {field('E-mail', <input style={inputStyle} value={form.email} onChange={set('email')} />)}
          {field('Téléphone', <input style={inputStyle} value={form.telephone || ''} onChange={set('telephone')} />)}
          {field('Numéro SIRET', <input style={inputStyle} value={form.siret || ''} onChange={set('siret')} placeholder="XXX XXX XXX XXXXX" />)}
        </div>
        <div style={{ marginTop: 14 }}>
          {field('Adresse postale', <input style={inputStyle} value={form.adresse || ''} onChange={set('adresse')} placeholder="Numéro, rue, code postal, ville" />)}
        </div>
        </>
      ))}

      {section('Préférences régionales', ("""

new_coords = """      {section('Coordonnées', (
        <>
        <div className="form-grid-2">
          {field('Nom affiché', <input style={inputStyle} value={form.nom} onChange={set('nom')} />)}
          {field('E-mail', <input style={inputStyle} value={form.email} onChange={set('email')} />)}
          {field('Téléphone', <input style={inputStyle} value={form.telephone || ''} onChange={set('telephone')} />)}
          {field('Numéro SIRET', <input style={inputStyle} value={form.siret || ''} onChange={set('siret')} placeholder="XXX XXX XXX XXXXX" />)}
        </div>
        <div style={{ marginTop: 14 }}>
          {field('Adresse postale', <input style={inputStyle} value={form.adresse || ''} onChange={set('adresse')} placeholder="Numéro, rue, code postal, ville" />)}
        </div>
        </>
      ))}

      {section('Coordonnées bancaires (pour vos factures)', (
        <>
        <div className="form-grid-2">
          {field('IBAN', <input style={inputStyle} value={form.iban || ''} onChange={set('iban')} placeholder="FR76 XXXX XXXX XXXX XXXX XXXX XXX" />)}
          {field('BIC', <input style={inputStyle} value={form.bic || ''} onChange={set('bic')} placeholder="XXXXFRPPXXX" />)}
        </div>
        <div style={{ marginTop: 14 }}>
          {field('Nom de la banque', <input style={inputStyle} value={form.banque || ''} onChange={set('banque')} placeholder="Ex: Caisse d'Épargne Rhône Alpes" />)}
        </div>
        </>
      ))}

      {section('Préférences régionales', ("""

if old_coords in content:
    content = content.replace(old_coords, new_coords)
    changes += 1
    print("OK 2/3 - Section Coordonnees bancaires ajoutee")
else:
    print("ERREUR 2/3 - Bloc Coordonnees non trouve")

# 3. Réécrire InvoiceModal au format complet de Victoria (avec RIB en bas)
old_invoice = """function InvoiceModal({ reservation, onClose, C, devise, settings }) {
  const invoiceNumber = `${String(reservation.id).slice(-6)}${new Date(reservation.date).getFullYear()}`;
  const todayStr = new Date().toLocaleDateString('fr-FR');
  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(10,18,27,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100, padding: 20 }} onClick={onClose}>
      <div style={{ background: '#fff', borderRadius: 14, width: '100%', maxWidth: 560, padding: 32 }} onClick={e => e.stopPropagation()}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 22 }}>
          <div style={{ fontSize: 13, lineHeight: 1.6, color: '#16232F' }}>
            <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 16 }}>{settings.nom}</div>
            {settings.adresse && <div>{settings.adresse}</div>}
            {settings.telephone && <div>{settings.telephone}</div>}
            {settings.email && <div>{settings.email}</div>}
            {settings.siret && <div>SIRET : {settings.siret}</div>}
          </div>
          <div style={{ textAlign: 'right', fontSize: 12.5, color: '#5A6B7A' }}>{todayStr}</div>
        </div>

        <div style={{ marginBottom: 20 }}>
          <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 15, color: '#10233D' }}>FACTURE n°{invoiceNumber}</div>
          <div style={{ fontSize: 13, color: '#5A6B7A', marginTop: 2 }}>{reservation.prenom} {reservation.nom}</div>
        </div>

        <div style={{ fontSize: 13.5, marginBottom: 16 }}>
          Cours de {reservation.discipline.toLowerCase()} à {reservation.station || ''} — {fmtDateShort(reservation.date)} ({reservation.heureDebut}–{reservation.heureFin})
        </div>

        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 15, fontWeight: 700, color: '#10233D', marginBottom: 6 }}>
          <span>TOTAL TTC</span><span>{fmtEUR(reservation.prix, devise)}</span>
        </div>
        <div style={{ fontSize: 12, color: '#5A6B7A', marginBottom: 26 }}>TVA non applicable, article 293 B du CGI</div>

        {reservation.modePaiement && reservation.modePaiement !== 'Non renseigné' && (
          <div style={{ fontSize: 12.5, color: '#5A6B7A', marginBottom: 20 }}>Réglé en direct — {reservation.modePaiement}</div>
        )}

        <button onClick={() => window.print()} style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, width: '100%', background: '#10233D', color: '#fff', border: 'none', borderRadius: 9, padding: '11px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}><Printer size={15} /> Imprimer / Enregistrer en PDF</button>
        <button onClick={onClose} style={{ display: 'block', margin: '10px auto 0', background: 'none', border: 'none', cursor: 'pointer', color: '#5A6B7A', fontSize: 13 }}>Fermer</button>
      </div>
    </div>
  );
}"""

new_invoice = """function InvoiceModal({ reservation, onClose, C, devise, settings }) {
  const invoiceNumber = `${String(reservation.id).slice(-6)}${new Date(reservation.date).getFullYear()}`;
  const todayStr = new Date().toLocaleDateString('fr-FR');
  const hasBank = settings.iban || settings.bic || settings.banque;
  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(10,18,27,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100, padding: 20 }} onClick={onClose}>
      <div style={{ background: '#fff', borderRadius: 14, width: '100%', maxWidth: 560, padding: 32 }} onClick={e => e.stopPropagation()}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 22 }}>
          <div style={{ fontSize: 13, lineHeight: 1.6, color: '#16232F' }}>
            <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 16 }}>{settings.nom}{settings.profession ? `. ${settings.profession}` : ''}</div>
            {settings.adresse && <div>{settings.adresse}</div>}
            {settings.telephone && <div>{settings.telephone}</div>}
            {settings.email && <div>{settings.email}</div>}
            {settings.siret && <div>SIRET : {settings.siret}</div>}
          </div>
          <div style={{ textAlign: 'right', fontSize: 12.5, color: '#5A6B7A' }}>{todayStr}</div>
        </div>

        <div style={{ textAlign: 'center', marginBottom: 20 }}>
          <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 15, color: '#10233D' }}>INVOICE n°{invoiceNumber}</div>
          <div style={{ fontSize: 13.5, fontWeight: 700, color: '#16232F', marginTop: 4 }}>{reservation.prenom} {reservation.nom}</div>
        </div>

        <div style={{ fontSize: 13.5, marginBottom: 10 }}>
          Cours de {reservation.discipline.toLowerCase()} à {reservation.station || ''} — {fmtDateShort(reservation.date)} ({reservation.heureDebut}–{reservation.heureFin})
        </div>

        <div style={{ textAlign: 'center', marginTop: 18, marginBottom: 6 }}>
          <div style={{ fontSize: 15, fontWeight: 700, color: '#10233D' }}>TOTAL TTC : {fmtEUR(reservation.prix, devise)}</div>
          <div style={{ fontSize: 12, fontStyle: 'italic', color: '#5A6B7A', marginTop: 4 }}>TVA non applicable, article 293 B du CGI</div>
        </div>

        {reservation.modePaiement && reservation.modePaiement !== 'Non renseigné' && (
          <div style={{ fontSize: 12.5, color: '#5A6B7A', textAlign: 'center', marginTop: 14 }}>Réglé en direct — {reservation.modePaiement}</div>
        )}

        {hasBank && (
          <div style={{ marginTop: 26, paddingTop: 18, borderTop: `1px solid #D3DEE6`, fontSize: 12, color: '#5A6B7A', lineHeight: 1.7 }}>
            <div style={{ fontWeight: 700, color: '#16232F', marginBottom: 6 }}>Relevé d'Identité Bancaire</div>
            <div>Titulaire du compte : {settings.nom}</div>
            {settings.iban && <div>IBAN : {settings.iban}</div>}
            {settings.bic && <div>BIC : {settings.bic}</div>}
            {settings.banque && <div>Banque : {settings.banque}</div>}
          </div>
        )}

        <button onClick={() => window.print()} style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, width: '100%', background: '#10233D', color: '#fff', border: 'none', borderRadius: 9, padding: '11px', fontSize: 14, fontWeight: 600, cursor: 'pointer', marginTop: 26 }}><Printer size={15} /> Imprimer / Enregistrer en PDF</button>
        <button onClick={onClose} style={{ display: 'block', margin: '10px auto 0', background: 'none', border: 'none', cursor: 'pointer', color: '#5A6B7A', fontSize: 13 }}>Fermer</button>
      </div>
    </div>
  );
}"""

if old_invoice in content:
    content = content.replace(old_invoice, new_invoice)
    changes += 1
    print("OK 3/3 - InvoiceModal mis a jour avec RIB")
else:
    print("ERREUR 3/3 - Bloc InvoiceModal non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/3 modifications appliquees.")
