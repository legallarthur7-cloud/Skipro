with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

old_pv = """function ParametresView({ settings, onSave, C, subscribed }) {
  const [form, setForm] = useState(settings);
  const [saved, setSaved] = useState(false);
  const [subLoading, setSubLoading] = useState(false);
  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }));

  const handleSubscribe = async () => {
    setSubLoading(true);
    try {
      const res = await fetch('/api/create-checkout-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: form.email }),
      });
      const data = await res.json();
      if (data.url) window.location.href = data.url;
      else { alert('Erreur : ' + (data.error || 'inconnue')); setSubLoading(false); }
    } catch (e) {
      alert('Erreur de connexion à Stripe.');
      setSubLoading(false);
    }
  };
  const toggleJour = (j) => setForm(f => ({ ...f, joursRepos: f.joursRepos.includes(j) ? f.joursRepos.filter(x => x !== j) : [...f.joursRepos, j] }));
  const inputStyle = { border: `1px solid ${C.iceLine}`, borderRadius: 8, padding: '9px 11px', fontSize: 14, background: C.card, color: C.ink, width: '100%' };
  const section = (title, content) => (
    <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px', display: 'flex', flexDirection: 'column', gap: 14 }}>
      <div style={{ fontSize: 14, fontWeight: 700, color: C.navy }}>{title}</div>
      {content}
    </div>
  );
  const field = (label, input) => <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}><label style={{ fontSize: 12, fontWeight: 600, color: C.inkSoft }}>{label}</label>{input}</div>;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18, maxWidth: 780 }}>
      <div>
        <h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>Paramètres</h1>
        <p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>Personnalisez votre compte et vos tarifs</p>
      </div>

      {section('Abonnement', (
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: 14 }}>
          <div>
            <div style={{ fontSize: 15, fontWeight: 700, color: C.navy }}>SkiPro — 29€/mois</div>
            <div style={{ fontSize: 13, color: C.inkSoft, marginTop: 2 }}>Toutes les fonctionnalités incluses. Résiliable à tout moment.</div>
          </div>
          {subscribed ? (
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, background: '#E6F4EA', color: '#1E7A3D', borderRadius: 9, padding: '11px 18px', fontSize: 14, fontWeight: 600 }}>
              ✓ Abonnement actif
            </div>
          ) : (
            <button onClick={handleSubscribe} disabled={subLoading} style={{ background: '#2E6F8E', color: '#fff', border: 'none', borderRadius: 9, padding: '11px 22px', fontSize: 14, fontWeight: 600, cursor: subLoading ? 'default' : 'pointer', opacity: subLoading ? 0.7 : 1 }}>
              {subLoading ? 'Un instant...' : "S'abonner"}
            </button>
          )}
        </div>
      ))}

      <BlurGate subscribed={subscribed} C={C}>
      {section('Coordonnées', (
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

      {section('Préférences régionales', (
        <div className="form-grid-3">
          {field('Devise', <select style={inputStyle} value={form.devise} onChange={set('devise')}><option value="EUR">Euro (€)</option><option value="CHF">Franc suisse (CHF)</option><option value="USD">Dollar ($)</option></select>)}
          {field('Langue de l\\'interface', <select style={inputStyle} value={form.langue} onChange={set('langue')}><option>Français</option><option>Anglais</option><option>Espagnol</option><option>Italien</option><option>Portugais</option></select>)}
          {field('Fuseau horaire', <select style={inputStyle} value={form.fuseauHoraire} onChange={set('fuseauHoraire')}><option value="Europe/Paris">Europe/Paris</option><option value="Europe/Zurich">Europe/Zurich</option></select>)}
        </div>
      ))}

      {section('Périodes de saison', (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          <div style={{ display: 'flex', gap: 8 }}>
            <button type="button" onClick={() => setForm(f => ({ ...f, seasonMode: 'vacances' }))} style={{ flex: 1, padding: '9px 12px', borderRadius: 9, cursor: 'pointer', fontSize: 13.5, fontWeight: 600, border: `1px solid ${form.seasonMode === 'vacances' ? ACCENTS.glacier : C.iceLine}`, background: form.seasonMode === 'vacances' ? ACCENTS.glacier + '18' : C.card, color: form.seasonMode === 'vacances' ? ACCENTS.glacierDeep : C.ink }}>Vacances scolaires (auto)</button>
            <button type="button" onClick={() => setForm(f => ({ ...f, seasonMode: 'manuel' }))} style={{ flex: 1, padding: '9px 12px', borderRadius: 9, cursor: 'pointer', fontSize: 13.5, fontWeight: 600, border: `1px solid ${form.seasonMode === 'manuel' ? ACCENTS.glacier : C.iceLine}`, background: form.seasonMode === 'manuel' ? ACCENTS.glacier + '18' : C.card, color: form.seasonMode === 'manuel' ? ACCENTS.glacierDeep : C.ink }}>Période manuelle</button>
          </div>

          {form.seasonMode === 'vacances' ? (
            <div>
              {field('Zone académique de référence', (
                <select style={inputStyle} value={form.zoneVacances} onChange={set('zoneVacances')}>
                  <option value="Toutes">Toutes les zones (recommandé pour une clientèle nationale)</option>
                  <option value="A">Zone A</option>
                  <option value="B">Zone B</option>
                  <option value="C">Zone C</option>
                </select>
              ))}
              <p style={{ fontSize: 12.5, color: C.inkSoft, marginTop: 10 }}>
                La haute saison correspond automatiquement aux vacances de Noël, d'Hiver et de Printemps (dates officielles Éducation nationale 2025-2026 et 2026-2027). "Toutes les zones" prend la période la plus large, utile si vos clients viennent de toute la France.
              </p>
            </div>
          ) : (
            <div>
              <div className="form-grid-2">
                {field('Début haute saison (MM-JJ)', <input style={inputStyle} placeholder="12-20" value={form.hauteSaisonDebut} onChange={set('hauteSaisonDebut')} />)}
                {field('Fin haute saison (MM-JJ)', <input style={inputStyle} placeholder="02-28" value={form.hauteSaisonFin} onChange={set('hauteSaisonFin')} />)}
              </div>
              <p style={{ fontSize: 12.5, color: C.inkSoft, marginTop: 10 }}>Toute date hors de cette période est considérée en basse saison.</p>
            </div>
          )}
        </div>
      ))}

      {section('Tarifs horaires', (
        <div className="form-grid-2">
          {field(`Ski — Haute saison (${form.devise}/h)`, <input type="number" style={inputStyle} value={form.tarifSkiHaute} onChange={set('tarifSkiHaute')} />)}
          {field(`Ski — Basse saison (${form.devise}/h)`, <input type="number" style={inputStyle} value={form.tarifSkiBasse} onChange={set('tarifSkiBasse')} />)}
          {field(`Snowboard — Haute saison (${form.devise}/h)`, <input type="number" style={inputStyle} value={form.tarifSnowboardHaute} onChange={set('tarifSnowboardHaute')} />)}
          {field(`Snowboard — Basse saison (${form.devise}/h)`, <input type="number" style={inputStyle} value={form.tarifSnowboardBasse} onChange={set('tarifSnowboardBasse')} />)}
        </div>
      ))}

      {section('Tarifs forfaitaires', (
        <div className="form-grid-2">
          {field(`Demi-journée — Haute saison (${form.devise})`, <input type="number" style={inputStyle} value={form.tarifDemiJourneeHaute} onChange={set('tarifDemiJourneeHaute')} />)}
          {field(`Demi-journée — Basse saison (${form.devise})`, <input type="number" style={inputStyle} value={form.tarifDemiJourneeBasse} onChange={set('tarifDemiJourneeBasse')} />)}
          {field(`Journée — Haute saison (${form.devise})`, <input type="number" style={inputStyle} value={form.tarifJourneeHaute} onChange={set('tarifJourneeHaute')} />)}
          {field(`Journée — Basse saison (${form.devise})`, <input type="number" style={inputStyle} value={form.tarifJourneeBasse} onChange={set('tarifJourneeBasse')} />)}
        </div>
      ))}

      {section('Horaires des demi-journées', (
        <div className="form-grid-2">
          {field('Matin — début', <input type="time" style={inputStyle} value={form.matinDebut || '09:00'} onChange={set('matinDebut')} />)}
          {field('Matin — fin', <input type="time" style={inputStyle} value={form.matinFin || '12:30'} onChange={set('matinFin')} />)}
          {field('Après-midi — début', <input type="time" style={inputStyle} value={form.apresMidiDebut || '13:30'} onChange={set('apresMidiDebut')} />)}
          {field('Après-midi — fin', <input type="time" style={inputStyle} value={form.apresMidiFin || '17:00'} onChange={set('apresMidiFin')} />)}
        </div>
      ))}

      {section('Jours de repos', (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
          {JOURS.map(j => (
            <button key={j} onClick={() => toggleJour(j)} style={{ padding: '7px 14px', borderRadius: 100, border: `1px solid ${form.joursRepos.includes(j) ? ACCENTS.glacier : C.iceLine}`, background: form.joursRepos.includes(j) ? ACCENTS.glacier + '18' : C.card, color: form.joursRepos.includes(j) ? ACCENTS.glacierDeep : C.ink, fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>{j}</button>
          ))}
        </div>
      ))}

      {section('Apparence', (
        <div style={{ display: 'flex', gap: 10 }}>
          <button onClick={() => setForm(f => ({ ...f, theme: 'light' }))} style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '9px 16px', borderRadius: 9, border: `1px solid ${form.theme === 'light' ? ACCENTS.glacier : C.iceLine}`, background: form.theme === 'light' ? ACCENTS.glacier + '18' : C.card, color: C.ink, cursor: 'pointer', fontSize: 13.5, fontWeight: 600 }}><Sun size={15} /> Clair</button>
          <button onClick={() => setForm(f => ({ ...f, theme: 'dark' }))} style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '9px 16px', borderRadius: 9, border: `1px solid ${form.theme === 'dark' ? ACCENTS.glacier : C.iceLine}`, background: form.theme === 'dark' ? ACCENTS.glacier + '18' : C.card, color: C.ink, cursor: 'pointer', fontSize: 13.5, fontWeight: 600 }}><Moon size={15} /> Sombre</button>
        </div>
      ))}

      {section('Notifications', (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <label style={{ display: 'flex', alignItems: 'center', gap: 10, fontSize: 14, color: C.ink }}><input type="checkbox" checked={form.notifEmail} onChange={e => setForm(f => ({ ...f, notifEmail: e.target.checked }))} /> Recevoir les confirmations par e-mail</label>
          <label style={{ display: 'flex', alignItems: 'center', gap: 10, fontSize: 14, color: C.ink }}><input type="checkbox" checked={form.notifSMS} onChange={e => setForm(f => ({ ...f, notifSMS: e.target.checked }))} /> Recevoir les rappels par SMS</label>
        </div>
      ))}

      <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
        <button onClick={() => { onSave(form); setSaved(true); setTimeout(() => setSaved(false), 2000); }} style={{ background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '10px 22px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}>Enregistrer</button>
        {saved && <span style={{ fontSize: 13.5, color: ACCENTS.green, fontWeight: 600 }}>Paramètres enregistrés ✓</span>}
      </div>
      </BlurGate>
    </div>
  );
}"""

new_pv = """function ParametresView({ settings, onSave, C, subscribed }) {
  const langue = settings.langue;
  const [form, setForm] = useState(settings);
  const [saved, setSaved] = useState(false);
  const [subLoading, setSubLoading] = useState(false);
  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }));

  const handleSubscribe = async () => {
    setSubLoading(true);
    try {
      const res = await fetch('/api/create-checkout-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: form.email }),
      });
      const data = await res.json();
      if (data.url) window.location.href = data.url;
      else { alert('Erreur : ' + (data.error || 'inconnue')); setSubLoading(false); }
    } catch (e) {
      alert('Erreur de connexion à Stripe.');
      setSubLoading(false);
    }
  };
  const toggleJour = (j) => setForm(f => ({ ...f, joursRepos: f.joursRepos.includes(j) ? f.joursRepos.filter(x => x !== j) : [...f.joursRepos, j] }));
  const inputStyle = { border: `1px solid ${C.iceLine}`, borderRadius: 8, padding: '9px 11px', fontSize: 14, background: C.card, color: C.ink, width: '100%' };
  const section = (title, content) => (
    <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 14, padding: '20px 22px', display: 'flex', flexDirection: 'column', gap: 14 }}>
      <div style={{ fontSize: 14, fontWeight: 700, color: C.navy }}>{title}</div>
      {content}
    </div>
  );
  const field = (label, input) => <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}><label style={{ fontSize: 12, fontWeight: 600, color: C.inkSoft }}>{label}</label>{input}</div>;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 18, maxWidth: 780 }}>
      <div>
        <h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 24, fontWeight: 700, color: C.navy }}>{tUI('parametres', langue)}</h1>
        <p style={{ fontSize: 14, color: C.inkSoft, marginTop: 4 }}>{tUI('settingsSubtitle', langue)}</p>
      </div>

      {section(tUI('sectionSubscription', langue), (
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: 14 }}>
          <div>
            <div style={{ fontSize: 15, fontWeight: 700, color: C.navy }}>SkiPro — 29€/mois</div>
            <div style={{ fontSize: 13, color: C.inkSoft, marginTop: 2 }}>{tUI('subscriptionDesc', langue)}</div>
          </div>
          {subscribed ? (
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, background: '#E6F4EA', color: '#1E7A3D', borderRadius: 9, padding: '11px 18px', fontSize: 14, fontWeight: 600 }}>
              ✓ {tUI('activeSubscription', langue)}
            </div>
          ) : (
            <button onClick={handleSubscribe} disabled={subLoading} style={{ background: '#2E6F8E', color: '#fff', border: 'none', borderRadius: 9, padding: '11px 22px', fontSize: 14, fontWeight: 600, cursor: subLoading ? 'default' : 'pointer', opacity: subLoading ? 0.7 : 1 }}>
              {subLoading ? tUI('loadingWait', langue) : tUI('btnSubscribe', langue)}
            </button>
          )}
        </div>
      ))}

      <BlurGate subscribed={subscribed} C={C}>
      {section(tUI('sectionCoordonnees', langue), (
        <>
        <div className="form-grid-2">
          {field(tUI('labelNomAffiche', langue), <input style={inputStyle} value={form.nom} onChange={set('nom')} />)}
          {field(tUI('fEmail', langue), <input style={inputStyle} value={form.email} onChange={set('email')} />)}
          {field(tUI('fTelephone', langue), <input style={inputStyle} value={form.telephone || ''} onChange={set('telephone')} />)}
          {field(tUI('labelSiret', langue), <input style={inputStyle} value={form.siret || ''} onChange={set('siret')} placeholder="XXX XXX XXX XXXXX" />)}
        </div>
        <div style={{ marginTop: 14 }}>
          {field(tUI('labelAdressePostale', langue), <input style={inputStyle} value={form.adresse || ''} onChange={set('adresse')} placeholder="Numéro, rue, code postal, ville" />)}
        </div>
        </>
      ))}

      {section(tUI('sectionBanque', langue), (
        <>
        <div className="form-grid-2">
          {field('IBAN', <input style={inputStyle} value={form.iban || ''} onChange={set('iban')} placeholder="FR76 XXXX XXXX XXXX XXXX XXXX XXX" />)}
          {field('BIC', <input style={inputStyle} value={form.bic || ''} onChange={set('bic')} placeholder="XXXXFRPPXXX" />)}
        </div>
        <div style={{ marginTop: 14 }}>
          {field(tUI('labelNomBanque', langue), <input style={inputStyle} value={form.banque || ''} onChange={set('banque')} placeholder="Ex: Caisse d'Épargne Rhône Alpes" />)}
        </div>
        </>
      ))}

      {section(tUI('sectionRegional', langue), (
        <div className="form-grid-3">
          {field(tUI('labelDevise', langue), <select style={inputStyle} value={form.devise} onChange={set('devise')}><option value="EUR">Euro (€)</option><option value="CHF">Franc suisse (CHF)</option><option value="USD">Dollar ($)</option></select>)}
          {field(tUI('labelLangueInterface', langue), <select style={inputStyle} value={form.langue} onChange={set('langue')}><option>Français</option><option>Anglais</option><option>Espagnol</option><option>Italien</option><option>Portugais</option></select>)}
          {field(tUI('labelFuseau', langue), <select style={inputStyle} value={form.fuseauHoraire} onChange={set('fuseauHoraire')}><option value="Europe/Paris">Europe/Paris</option><option value="Europe/Zurich">Europe/Zurich</option></select>)}
        </div>
      ))}

      {section(tUI('sectionSaisons', langue), (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          <div style={{ display: 'flex', gap: 8 }}>
            <button type="button" onClick={() => setForm(f => ({ ...f, seasonMode: 'vacances' }))} style={{ flex: 1, padding: '9px 12px', borderRadius: 9, cursor: 'pointer', fontSize: 13.5, fontWeight: 600, border: `1px solid ${form.seasonMode === 'vacances' ? ACCENTS.glacier : C.iceLine}`, background: form.seasonMode === 'vacances' ? ACCENTS.glacier + '18' : C.card, color: form.seasonMode === 'vacances' ? ACCENTS.glacierDeep : C.ink }}>{tUI('btnVacancesAuto', langue)}</button>
            <button type="button" onClick={() => setForm(f => ({ ...f, seasonMode: 'manuel' }))} style={{ flex: 1, padding: '9px 12px', borderRadius: 9, cursor: 'pointer', fontSize: 13.5, fontWeight: 600, border: `1px solid ${form.seasonMode === 'manuel' ? ACCENTS.glacier : C.iceLine}`, background: form.seasonMode === 'manuel' ? ACCENTS.glacier + '18' : C.card, color: form.seasonMode === 'manuel' ? ACCENTS.glacierDeep : C.ink }}>{tUI('btnPeriodeManuelle', langue)}</button>
          </div>

          {form.seasonMode === 'vacances' ? (
            <div>
              {field(tUI('labelZoneAcademique', langue), (
                <select style={inputStyle} value={form.zoneVacances} onChange={set('zoneVacances')}>
                  <option value="Toutes">{tUI('optToutesZones', langue)}</option>
                  <option value="A">Zone A</option>
                  <option value="B">Zone B</option>
                  <option value="C">Zone C</option>
                </select>
              ))}
              <p style={{ fontSize: 12.5, color: C.inkSoft, marginTop: 10 }}>
                {tUI('seasonExplainAuto', langue)}
              </p>
            </div>
          ) : (
            <div>
              <div className="form-grid-2">
                {field(tUI('labelDebutHauteSaison', langue), <input style={inputStyle} placeholder="12-20" value={form.hauteSaisonDebut} onChange={set('hauteSaisonDebut')} />)}
                {field(tUI('labelFinHauteSaison', langue), <input style={inputStyle} placeholder="02-28" value={form.hauteSaisonFin} onChange={set('hauteSaisonFin')} />)}
              </div>
              <p style={{ fontSize: 12.5, color: C.inkSoft, marginTop: 10 }}>{tUI('seasonExplainManual', langue)}</p>
            </div>
          )}
        </div>
      ))}

      {section(tUI('sectionTarifsHoraires', langue), (
        <div className="form-grid-2">
          {field(`Ski — ${tUI('highSeason', langue)} (${form.devise}/h)`, <input type="number" style={inputStyle} value={form.tarifSkiHaute} onChange={set('tarifSkiHaute')} />)}
          {field(`Ski — ${tUI('lowSeason', langue)} (${form.devise}/h)`, <input type="number" style={inputStyle} value={form.tarifSkiBasse} onChange={set('tarifSkiBasse')} />)}
          {field(`Snowboard — ${tUI('highSeason', langue)} (${form.devise}/h)`, <input type="number" style={inputStyle} value={form.tarifSnowboardHaute} onChange={set('tarifSnowboardHaute')} />)}
          {field(`Snowboard — ${tUI('lowSeason', langue)} (${form.devise}/h)`, <input type="number" style={inputStyle} value={form.tarifSnowboardBasse} onChange={set('tarifSnowboardBasse')} />)}
        </div>
      ))}

      {section(tUI('sectionTarifsForfait', langue), (
        <div className="form-grid-2">
          {field(`${tUI('engDemiJournee', langue)} — ${tUI('highSeason', langue)} (${form.devise})`, <input type="number" style={inputStyle} value={form.tarifDemiJourneeHaute} onChange={set('tarifDemiJourneeHaute')} />)}
          {field(`${tUI('engDemiJournee', langue)} — ${tUI('lowSeason', langue)} (${form.devise})`, <input type="number" style={inputStyle} value={form.tarifDemiJourneeBasse} onChange={set('tarifDemiJourneeBasse')} />)}
          {field(`${tUI('engJournee', langue)} — ${tUI('highSeason', langue)} (${form.devise})`, <input type="number" style={inputStyle} value={form.tarifJourneeHaute} onChange={set('tarifJourneeHaute')} />)}
          {field(`${tUI('engJournee', langue)} — ${tUI('lowSeason', langue)} (${form.devise})`, <input type="number" style={inputStyle} value={form.tarifJourneeBasse} onChange={set('tarifJourneeBasse')} />)}
        </div>
      ))}

      {section(tUI('sectionHorairesDemi', langue), (
        <div className="form-grid-2">
          {field(`${tUI('crenMatin', langue)} — ${tUI('labelDebut', langue)}`, <input type="time" style={inputStyle} value={form.matinDebut || '09:00'} onChange={set('matinDebut')} />)}
          {field(`${tUI('crenMatin', langue)} — ${tUI('labelFin', langue)}`, <input type="time" style={inputStyle} value={form.matinFin || '12:30'} onChange={set('matinFin')} />)}
          {field(`${tUI('crenApresMidi', langue)} — ${tUI('labelDebut', langue)}`, <input type="time" style={inputStyle} value={form.apresMidiDebut || '13:30'} onChange={set('apresMidiDebut')} />)}
          {field(`${tUI('crenApresMidi', langue)} — ${tUI('labelFin', langue)}`, <input type="time" style={inputStyle} value={form.apresMidiFin || '17:00'} onChange={set('apresMidiFin')} />)}
        </div>
      ))}

      {section(tUI('sectionJoursRepos', langue), (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
          {JOURS.map(j => (
            <button key={j} onClick={() => toggleJour(j)} style={{ padding: '7px 14px', borderRadius: 100, border: `1px solid ${form.joursRepos.includes(j) ? ACCENTS.glacier : C.iceLine}`, background: form.joursRepos.includes(j) ? ACCENTS.glacier + '18' : C.card, color: form.joursRepos.includes(j) ? ACCENTS.glacierDeep : C.ink, fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>{j}</button>
          ))}
        </div>
      ))}

      {section(tUI('sectionApparence', langue), (
        <div style={{ display: 'flex', gap: 10 }}>
          <button onClick={() => setForm(f => ({ ...f, theme: 'light' }))} style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '9px 16px', borderRadius: 9, border: `1px solid ${form.theme === 'light' ? ACCENTS.glacier : C.iceLine}`, background: form.theme === 'light' ? ACCENTS.glacier + '18' : C.card, color: C.ink, cursor: 'pointer', fontSize: 13.5, fontWeight: 600 }}><Sun size={15} /> {tUI('btnClair', langue)}</button>
          <button onClick={() => setForm(f => ({ ...f, theme: 'dark' }))} style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '9px 16px', borderRadius: 9, border: `1px solid ${form.theme === 'dark' ? ACCENTS.glacier : C.iceLine}`, background: form.theme === 'dark' ? ACCENTS.glacier + '18' : C.card, color: C.ink, cursor: 'pointer', fontSize: 13.5, fontWeight: 600 }}><Moon size={15} /> {tUI('btnSombre', langue)}</button>
        </div>
      ))}

      {section(tUI('sectionNotifications', langue), (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <label style={{ display: 'flex', alignItems: 'center', gap: 10, fontSize: 14, color: C.ink }}><input type="checkbox" checked={form.notifEmail} onChange={e => setForm(f => ({ ...f, notifEmail: e.target.checked }))} /> {tUI('notifEmailLabel', langue)}</label>
          <label style={{ display: 'flex', alignItems: 'center', gap: 10, fontSize: 14, color: C.ink }}><input type="checkbox" checked={form.notifSMS} onChange={e => setForm(f => ({ ...f, notifSMS: e.target.checked }))} /> {tUI('notifSmsLabel', langue)}</label>
        </div>
      ))}

      <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
        <button onClick={() => { onSave(form); setSaved(true); setTimeout(() => setSaved(false), 2000); }} style={{ background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '10px 22px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}>{tUI('btnSave', langue)}</button>
        {saved && <span style={{ fontSize: 13.5, color: ACCENTS.green, fontWeight: 600 }}>{tUI('settingsSaved', langue)}</span>}
      </div>
      </BlurGate>
    </div>
  );
}"""

if old_pv in content:
    content = content.replace(old_pv, new_pv, 1)
    changes += 1
    print("OK - ParametresView traduit")
else:
    print("ERREUR - ParametresView non trouve (verifier correspondance exacte)")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes} modifications appliquees (Etape 9b/N - composant Parametres).")
