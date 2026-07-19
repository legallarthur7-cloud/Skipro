import re

with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

# 1. Ajouter les nouveaux champs à DEFAULT_SETTINGS
old_settings = """const DEFAULT_SETTINGS = {
  nom: 'Moniteur ESF', email: 'contact@exemple.com', devise: 'EUR', langue: 'Français',
  fuseauHoraire: 'Europe/Paris',"""

new_settings = """const DEFAULT_SETTINGS = {
  nom: 'Moniteur ESF', email: 'contact@exemple.com', devise: 'EUR', langue: 'Français',
  fuseauHoraire: 'Europe/Paris',
  adresse: '', telephone: '', siret: '',"""

if old_settings in content:
    content = content.replace(old_settings, new_settings)
    changes += 1
    print("✅ 1/3 - DEFAULT_SETTINGS mis à jour")
else:
    print("❌ 1/3 - Bloc DEFAULT_SETTINGS non trouvé")

# 2. Ajouter les champs dans la section Coordonnées
old_coords = """      {section('Coordonnées', (
        <div className="form-grid-2">
          {field('Nom affiché', <input style={inputStyle} value={form.nom} onChange={set('nom')} />)}
          {field('E-mail', <input style={inputStyle} value={form.email} onChange={set('email')} />)}
        </div>
      ))}"""

new_coords = """      {section('Coordonnées', (
        <div className="form-grid-2">
          {field('Nom affiché', <input style={inputStyle} value={form.nom} onChange={set('nom')} />)}
          {field('E-mail', <input style={inputStyle} value={form.email} onChange={set('email')} />)}
          {field('Téléphone', <input style={inputStyle} value={form.telephone || ''} onChange={set('telephone')} />)}
          {field('Numéro SIRET', <input style={inputStyle} value={form.siret || ''} onChange={set('siret')} placeholder="XXX XXX XXX XXXXX" />)}
        </div>
        <div style={{ marginTop: 14 }}>
          {field('Adresse postale', <input style={inputStyle} value={form.adresse || ''} onChange={set('adresse')} placeholder="Numéro, rue, code postal, ville" />)}
        </div>
      ))}"""

if old_coords in content:
    content = content.replace(old_coords, new_coords)
    changes += 1
    print("✅ 2/3 - Section Coordonnées mise à jour")
else:
    print("❌ 2/3 - Bloc Coordonnées non trouvé")

# 3. Réécrire InvoiceModal au format Victoria
old_invoice = """function InvoiceModal({ reservation, onClose, C, devise, settings }) {
  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(10,18,27,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100, padding: 20 }} onClick={onClose}>
      <div style={{ background: '#fff', borderRadius: 14, width: '100%', maxWidth: 520, padding: 32 }} onClick={e => e.stopPropagation()}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 26 }}>
          <div><div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 20, color: '#10233D' }}>Facture</div><div style={{ fontSize: 12.5, color: '#5A6B7A', marginTop: 2 }}>N° {String(reservation.id).slice(-6)}</div></div>
          <button onClick={onClose} style={{ background: 'none', border: 'none', cursor: 'pointer', color: '#5A6B7A' }}><X size={18} /></button>
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 13, marginBottom: 20 }}>
          <div><div style={{ fontWeight: 700, marginBottom: 4 }}>Moniteur</div><div style={{ color: '#5A6B7A' }}>{settings.nom}<br />ESF · {reservation.station}</div></div>
          <div style={{ textAlign: 'right' }}><div style={{ fontWeight: 700, marginBottom: 4 }}>Client</div><div style={{ color: '#5A6B7A' }}>{reservation.prenom} {reservation.nom}<br />{reservation.email}</div></div>
        </div>
        <div style={{ border: '1px solid #D3DEE6', borderRadius: 10, overflow: 'hidden', marginBottom: 20 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', padding: '10px 14px', background: '#F0F3F6', fontSize: 12, fontWeight: 700, color: '#5A6B7A' }}><span>Prestation</span><span>Montant</span></div>
          <div style={{ display: 'flex', justifyContent: 'space-between', padding: '12px 14px', fontSize: 13.5 }}><span>Cours de {reservation.discipline.toLowerCase()} — {fmtDateShort(reservation.date)} ({reservation.heureDebut}–{reservation.heureFin})</span><span style={{ fontWeight: 700 }}>{fmtEUR(reservation.prix, devise)}</span></div>
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 15, fontWeight: 700, color: '#10233D', marginBottom: 10 }}><span>Total</span><span>{fmtEUR(reservation.prix, devise)}</span></div>
        {reservation.modePaiement && reservation.modePaiement !== 'Non renseigné' && (
          <div style={{ fontSize: 12.5, color: '#5A6B7A', marginBottom: 26 }}>Réglé en direct — {reservation.modePaiement}</div>
        )}
        <button onClick={() => window.print()} style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, width: '100%', background: '#10233D', color: '#fff', border: 'none', borderRadius: 9, padding: '11px', fontSize: 14, fontWeight: 600, cursor: 'pointer', marginTop: reservation.modePaiement && reservation.modePaiement !== 'Non renseigné' ? 0 : 26 }}><Printer size={15} /> Imprimer / Enregistrer en PDF</button>
      </div>
    </div>
  );
}"""

new_invoice = """function InvoiceModal({ reservation, onClose, C, devise, settings }) {
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

if old_invoice in content:
    content = content.replace(old_invoice, new_invoice)
    changes += 1
    print("✅ 3/3 - InvoiceModal mis à jour")
else:
    print("❌ 3/3 - Bloc InvoiceModal non trouvé")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/3 modifications appliquées.")
