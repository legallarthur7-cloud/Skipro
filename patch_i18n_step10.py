with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0

lang_anchors = [
    ("Français",
     "    notifSmsLabel: 'Recevoir les rappels par SMS', settingsSaved: 'Paramètres enregistrés ✓'\n  },",
     "    notifSmsLabel: 'Recevoir les rappels par SMS', settingsSaved: 'Paramètres enregistrés ✓',\n    authTabLogin: 'Connexion', authTabSignup: 'Inscription', authForgotTitle: 'Mot de passe oublié',\n    authForgotDesc: \"Indique ton e-mail, on t'enverra un lien de réinitialisation.\", authSendLink: 'Envoyer le lien',\n    authBackToLogin: 'Retour à la connexion',\n    authResetSent: \"Si un compte existe avec cette adresse, un lien de réinitialisation vient d'être envoyé.\",\n    authNamePlaceholder: 'Prénom et nom (ex: Julien Berthier)', authEmailPlaceholder: 'E-mail',\n    authPasswordPlaceholder: 'Mot de passe', authConfirmPasswordPlaceholder: 'Confirmer le mot de passe',\n    authForgotLink: 'Mot de passe oublié ?', authSubmitLogin: 'Se connecter', authSubmitSignup: 'Créer mon compte',\n    authPrototypeNote: \"Version prototype — l'authentification n'est pas encore reliée à une vraie base de données.\",\n    errFillAllFields: 'Merci de remplir tous les champs.', errPasswordsMismatch: 'Les mots de passe ne correspondent pas.',\n    successAccountCreated: 'Compte créé ! Vérifie tes e-mails pour confirmer ton adresse, puis connecte-toi.',\n    errFillEmailPassword: 'Merci de renseigner ton e-mail et ton mot de passe.'\n  },"),
    ("Anglais",
     "    notifSmsLabel: 'Receive reminders by SMS', settingsSaved: 'Settings saved ✓'\n  },",
     "    notifSmsLabel: 'Receive reminders by SMS', settingsSaved: 'Settings saved ✓',\n    authTabLogin: 'Login', authTabSignup: 'Sign up', authForgotTitle: 'Forgot password',\n    authForgotDesc: \"Enter your email, we'll send you a reset link.\", authSendLink: 'Send link',\n    authBackToLogin: 'Back to login',\n    authResetSent: 'If an account exists with this address, a reset link has just been sent.',\n    authNamePlaceholder: 'First and last name (e.g. Julien Berthier)', authEmailPlaceholder: 'Email',\n    authPasswordPlaceholder: 'Password', authConfirmPasswordPlaceholder: 'Confirm password',\n    authForgotLink: 'Forgot password?', authSubmitLogin: 'Log in', authSubmitSignup: 'Create my account',\n    authPrototypeNote: 'Prototype version — authentication is not yet connected to a real database.',\n    errFillAllFields: 'Please fill in all fields.', errPasswordsMismatch: 'Passwords do not match.',\n    successAccountCreated: 'Account created! Check your email to confirm your address, then log in.',\n    errFillEmailPassword: 'Please enter your email and password.'\n  },"),
    ("Espagnol",
     "    notifSmsLabel: 'Recibir recordatorios por SMS', settingsSaved: 'Ajustes guardados ✓'\n  },",
     "    notifSmsLabel: 'Recibir recordatorios por SMS', settingsSaved: 'Ajustes guardados ✓',\n    authTabLogin: 'Iniciar sesión', authTabSignup: 'Registrarse', authForgotTitle: 'Contraseña olvidada',\n    authForgotDesc: 'Indica tu correo, te enviaremos un enlace de restablecimiento.', authSendLink: 'Enviar enlace',\n    authBackToLogin: 'Volver al inicio de sesión',\n    authResetSent: 'Si existe una cuenta con esta dirección, se acaba de enviar un enlace de restablecimiento.',\n    authNamePlaceholder: 'Nombre y apellido (ej: Julien Berthier)', authEmailPlaceholder: 'Correo electrónico',\n    authPasswordPlaceholder: 'Contraseña', authConfirmPasswordPlaceholder: 'Confirmar contraseña',\n    authForgotLink: '¿Contraseña olvidada?', authSubmitLogin: 'Iniciar sesión', authSubmitSignup: 'Crear mi cuenta',\n    authPrototypeNote: 'Versión prototipo: la autenticación aún no está conectada a una base de datos real.',\n    errFillAllFields: 'Por favor completa todos los campos.', errPasswordsMismatch: 'Las contraseñas no coinciden.',\n    successAccountCreated: '¡Cuenta creada! Revisa tu correo para confirmar tu dirección y luego inicia sesión.',\n    errFillEmailPassword: 'Por favor ingresa tu correo y contraseña.'\n  },"),
    ("Italien",
     "    notifSmsLabel: 'Ricevi promemoria via SMS', settingsSaved: 'Impostazioni salvate ✓'\n  },",
     "    notifSmsLabel: 'Ricevi promemoria via SMS', settingsSaved: 'Impostazioni salvate ✓',\n    authTabLogin: 'Accedi', authTabSignup: 'Registrati', authForgotTitle: 'Password dimenticata',\n    authForgotDesc: 'Indica la tua e-mail, ti invieremo un link per reimpostarla.', authSendLink: 'Invia link',\n    authBackToLogin: 'Torna al login',\n    authResetSent: 'Se esiste un account con questo indirizzo, è appena stato inviato un link di reimpostazione.',\n    authNamePlaceholder: 'Nome e cognome (es: Julien Berthier)', authEmailPlaceholder: 'E-mail',\n    authPasswordPlaceholder: 'Password', authConfirmPasswordPlaceholder: 'Conferma password',\n    authForgotLink: 'Password dimenticata?', authSubmitLogin: 'Accedi', authSubmitSignup: 'Crea il mio account',\n    authPrototypeNote: \"Versione prototipo: l'autenticazione non è ancora collegata a un vero database.\",\n    errFillAllFields: 'Compila tutti i campi, per favore.', errPasswordsMismatch: 'Le password non corrispondono.',\n    successAccountCreated: 'Account creato! Controlla la tua e-mail per confermare il tuo indirizzo, poi accedi.',\n    errFillEmailPassword: 'Inserisci la tua e-mail e password.'\n  },"),
    ("Portugais",
     "    notifSmsLabel: 'Receber lembretes por SMS', settingsSaved: 'Configurações salvas ✓'\n  }\n};",
     "    notifSmsLabel: 'Receber lembretes por SMS', settingsSaved: 'Configurações salvas ✓',\n    authTabLogin: 'Entrar', authTabSignup: 'Cadastrar', authForgotTitle: 'Senha esquecida',\n    authForgotDesc: 'Informe seu e-mail, enviaremos um link de redefinição.', authSendLink: 'Enviar link',\n    authBackToLogin: 'Voltar ao login',\n    authResetSent: 'Se existir uma conta com este endereço, um link de redefinição acabou de ser enviado.',\n    authNamePlaceholder: 'Nome e sobrenome (ex: Julien Berthier)', authEmailPlaceholder: 'E-mail',\n    authPasswordPlaceholder: 'Senha', authConfirmPasswordPlaceholder: 'Confirmar senha',\n    authForgotLink: 'Esqueceu a senha?', authSubmitLogin: 'Entrar', authSubmitSignup: 'Criar minha conta',\n    authPrototypeNote: 'Versão protótipo — a autenticação ainda não está conectada a um banco de dados real.',\n    errFillAllFields: 'Por favor, preencha todos os campos.', errPasswordsMismatch: 'As senhas não coincidem.',\n    successAccountCreated: 'Conta criada! Verifique seu e-mail para confirmar seu endereço e depois faça login.',\n    errFillEmailPassword: 'Por favor, informe seu e-mail e senha.'\n  }\n};"),
]

for name, old, new in lang_anchors:
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"OK - Cles auth ajoutees pour {name}")
    else:
        print(f"ERREUR - Bloc {name} non trouve")

old_auth = """function AuthScreen({ onAuth }) {
  const [mode, setMode] = useState('login'); // 'login' | 'signup' | 'forgot'
  const [form, setForm] = useState({ nom: '', email: '', password: '', confirm: '' });
  const [error, setError] = useState('');
  const [sentReset, setSentReset] = useState(false);
  const [loading, setLoading] = useState(false);
  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }));
  const C = PALETTES.light;
  const inputStyle = { border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '10px 12px 10px 38px', fontSize: 14.5, fontFamily: 'Inter, sans-serif', color: C.ink, background: '#fff', width: '100%' };
  const wrapField = (icon, input) => <div style={{ position: 'relative' }}>{icon}{input}</div>;

  const handleSubmit = async () => {
    if (mode === 'signup') {
      if (!form.nom || !form.email || !form.password) { setError('Merci de remplir tous les champs.'); return; }
      if (form.password !== form.confirm) { setError('Les mots de passe ne correspondent pas.'); return; }
      setError(''); setLoading(true);
      const { error: signUpError } = await supabase.auth.signUp({
        email: form.email, password: form.password, options: { data: { nom: form.nom } }
      });
      setLoading(false);
      if (signUpError) { setError(signUpError.message); return; }
      setError('Compte créé ! Vérifie tes e-mails pour confirmer ton adresse, puis connecte-toi.');
      setMode('login');
      return;
    } else if (mode === 'login') {
      if (!form.email || !form.password) { setError('Merci de renseigner ton e-mail et ton mot de passe.'); return; }
      setError(''); setLoading(true);
      const { error: signInError } = await supabase.auth.signInWithPassword({ email: form.email, password: form.password });
      setLoading(false);
      if (signInError) { setError(signInError.message); return; }
      onAuth();
      return;
    }
  };

  return (
    <div style={{ minHeight: '100vh', background: C.snow, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 20, fontFamily: 'Inter, sans-serif' }}>
      <div style={{ width: '100%', maxWidth: 400 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 9, marginBottom: 28, fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 20, color: C.navy }}>
          <span style={{ width: 20, height: 20, borderRadius: 5, background: `linear-gradient(135deg, ${ACCENTS.green} 33%, ${ACCENTS.blue} 33% 66%, #000 66%)` }} />
          SkiPro
        </div>
        <div style={{ background: '#fff', border: `1px solid ${C.iceLine}`, borderRadius: 18, padding: 28, boxShadow: '0 24px 60px -30px rgba(16,35,61,0.25)' }}>
          {mode !== 'forgot' && (
            <div style={{ display: 'flex', border: `1px solid ${C.iceLine}`, borderRadius: 9, overflow: 'hidden', marginBottom: 22 }}>
              <button onClick={() => { setMode('login'); setError(''); }} style={{ flex: 1, padding: '9px 0', border: 'none', cursor: 'pointer', fontSize: 13.5, fontWeight: 600, background: mode === 'login' ? ACCENTS.glacier : '#fff', color: mode === 'login' ? '#fff' : C.ink }}>Connexion</button>
              <button onClick={() => { setMode('signup'); setError(''); }} style={{ flex: 1, padding: '9px 0', border: 'none', cursor: 'pointer', fontSize: 13.5, fontWeight: 600, background: mode === 'signup' ? ACCENTS.glacier : '#fff', color: mode === 'signup' ? '#fff' : C.ink }}>Inscription</button>
            </div>
          )}

          {mode === 'forgot' ? (
            sentReset ? (
              <div style={{ textAlign: 'center', padding: '10px 0' }}>
                <div style={{ fontSize: 14, color: C.ink, marginBottom: 18 }}>Si un compte existe avec cette adresse, un lien de réinitialisation vient d'être envoyé.</div>
                <button onClick={() => { setMode('login'); setSentReset(false); }} style={{ background: 'none', border: 'none', color: ACCENTS.glacierDeep, fontSize: 13.5, fontWeight: 600, cursor: 'pointer' }}>Retour à la connexion</button>
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
                <div>
                  <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 17, color: C.navy, marginBottom: 4 }}>Mot de passe oublié</div>
                  <div style={{ fontSize: 13, color: C.inkSoft }}>Indique ton e-mail, on t'enverra un lien de réinitialisation.</div>
                </div>
                {wrapField(<Mail size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input placeholder="E-mail" style={inputStyle} value={form.email} onChange={set('email')} />)}
                <button onClick={async () => { await supabase.auth.resetPasswordForEmail(form.email); setSentReset(true); }} style={{ background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '11px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}>Envoyer le lien</button>
                <button onClick={() => setMode('login')} style={{ background: 'none', border: 'none', color: C.inkSoft, fontSize: 13, cursor: 'pointer' }}>← Retour à la connexion</button>
              </div>
            )
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
              {mode === 'signup' && wrapField(<User size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input placeholder="Prénom et nom (ex: Julien Berthier)" style={inputStyle} value={form.nom} onChange={set('nom')} />)}
              {wrapField(<Mail size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input placeholder="E-mail" style={inputStyle} value={form.email} onChange={set('email')} />)}
              {wrapField(<Lock size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input type="password" placeholder="Mot de passe" style={inputStyle} value={form.password} onChange={set('password')} />)}
              {mode === 'signup' && wrapField(<Lock size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input type="password" placeholder="Confirmer le mot de passe" style={inputStyle} value={form.confirm} onChange={set('confirm')} />)}

              {mode === 'login' && (
                <div style={{ textAlign: 'right' }}>
                  <button onClick={() => { setMode('forgot'); setError(''); }} style={{ background: 'none', border: 'none', color: ACCENTS.glacierDeep, fontSize: 12.5, fontWeight: 600, cursor: 'pointer' }}>Mot de passe oublié ?</button>
                </div>
              )}

              {error && <div style={{ fontSize: 12.5, color: ACCENTS.red, background: ACCENTS.red + '12', borderRadius: 8, padding: '9px 11px' }}>{error}</div>}

              <button onClick={handleSubmit} disabled={loading} style={{ background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '11px', fontSize: 14, fontWeight: 600, cursor: loading ? 'default' : 'pointer', marginTop: 4, opacity: loading ? 0.7 : 1 }}>
                {loading ? 'Un instant...' : (mode === 'login' ? 'Se connecter' : 'Créer mon compte')}
              </button>
            </div>
          )}
        </div>
        <p style={{ textAlign: 'center', fontSize: 11.5, color: C.inkSoft, marginTop: 16 }}>Version prototype — l'authentification n'est pas encore reliée à une vraie base de données.</p>
      </div>
    </div>
  );
}"""

new_auth = """function AuthScreen({ onAuth }) {
  const [mode, setMode] = useState('login'); // 'login' | 'signup' | 'forgot'
  const [form, setForm] = useState({ nom: '', email: '', password: '', confirm: '' });
  const [error, setError] = useState('');
  const [sentReset, setSentReset] = useState(false);
  const [loading, setLoading] = useState(false);
  const [authLangue, setAuthLangue] = useState('Français');
  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }));
  const C = PALETTES.light;
  const inputStyle = { border: `1px solid ${C.iceLine}`, borderRadius: 9, padding: '10px 12px 10px 38px', fontSize: 14.5, fontFamily: 'Inter, sans-serif', color: C.ink, background: '#fff', width: '100%' };
  const wrapField = (icon, input) => <div style={{ position: 'relative' }}>{icon}{input}</div>;

  const handleSubmit = async () => {
    if (mode === 'signup') {
      if (!form.nom || !form.email || !form.password) { setError(tUI('errFillAllFields', authLangue)); return; }
      if (form.password !== form.confirm) { setError(tUI('errPasswordsMismatch', authLangue)); return; }
      setError(''); setLoading(true);
      const { error: signUpError } = await supabase.auth.signUp({
        email: form.email, password: form.password, options: { data: { nom: form.nom } }
      });
      setLoading(false);
      if (signUpError) { setError(signUpError.message); return; }
      setError(tUI('successAccountCreated', authLangue));
      setMode('login');
      return;
    } else if (mode === 'login') {
      if (!form.email || !form.password) { setError(tUI('errFillEmailPassword', authLangue)); return; }
      setError(''); setLoading(true);
      const { error: signInError } = await supabase.auth.signInWithPassword({ email: form.email, password: form.password });
      setLoading(false);
      if (signInError) { setError(signInError.message); return; }
      onAuth();
      return;
    }
  };

  return (
    <div style={{ minHeight: '100vh', background: C.snow, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 20, fontFamily: 'Inter, sans-serif' }}>
      <div style={{ width: '100%', maxWidth: 400 }}>
        <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: 8 }}>
          <select value={authLangue} onChange={e => setAuthLangue(e.target.value)} style={{ border: `1px solid ${C.iceLine}`, borderRadius: 8, padding: '5px 8px', fontSize: 12.5, color: C.inkSoft, background: '#fff' }}>
            <option>Français</option><option>Anglais</option><option>Espagnol</option><option>Italien</option><option>Portugais</option>
          </select>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 9, marginBottom: 28, fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 20, color: C.navy }}>
          <span style={{ width: 20, height: 20, borderRadius: 5, background: `linear-gradient(135deg, ${ACCENTS.green} 33%, ${ACCENTS.blue} 33% 66%, #000 66%)` }} />
          SkiPro
        </div>
        <div style={{ background: '#fff', border: `1px solid ${C.iceLine}`, borderRadius: 18, padding: 28, boxShadow: '0 24px 60px -30px rgba(16,35,61,0.25)' }}>
          {mode !== 'forgot' && (
            <div style={{ display: 'flex', border: `1px solid ${C.iceLine}`, borderRadius: 9, overflow: 'hidden', marginBottom: 22 }}>
              <button onClick={() => { setMode('login'); setError(''); }} style={{ flex: 1, padding: '9px 0', border: 'none', cursor: 'pointer', fontSize: 13.5, fontWeight: 600, background: mode === 'login' ? ACCENTS.glacier : '#fff', color: mode === 'login' ? '#fff' : C.ink }}>{tUI('authTabLogin', authLangue)}</button>
              <button onClick={() => { setMode('signup'); setError(''); }} style={{ flex: 1, padding: '9px 0', border: 'none', cursor: 'pointer', fontSize: 13.5, fontWeight: 600, background: mode === 'signup' ? ACCENTS.glacier : '#fff', color: mode === 'signup' ? '#fff' : C.ink }}>{tUI('authTabSignup', authLangue)}</button>
            </div>
          )}

          {mode === 'forgot' ? (
            sentReset ? (
              <div style={{ textAlign: 'center', padding: '10px 0' }}>
                <div style={{ fontSize: 14, color: C.ink, marginBottom: 18 }}>{tUI('authResetSent', authLangue)}</div>
                <button onClick={() => { setMode('login'); setSentReset(false); }} style={{ background: 'none', border: 'none', color: ACCENTS.glacierDeep, fontSize: 13.5, fontWeight: 600, cursor: 'pointer' }}>{tUI('authBackToLogin', authLangue)}</button>
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
                <div>
                  <div style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 17, color: C.navy, marginBottom: 4 }}>{tUI('authForgotTitle', authLangue)}</div>
                  <div style={{ fontSize: 13, color: C.inkSoft }}>{tUI('authForgotDesc', authLangue)}</div>
                </div>
                {wrapField(<Mail size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input placeholder={tUI('authEmailPlaceholder', authLangue)} style={inputStyle} value={form.email} onChange={set('email')} />)}
                <button onClick={async () => { await supabase.auth.resetPasswordForEmail(form.email); setSentReset(true); }} style={{ background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '11px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}>{tUI('authSendLink', authLangue)}</button>
                <button onClick={() => setMode('login')} style={{ background: 'none', border: 'none', color: C.inkSoft, fontSize: 13, cursor: 'pointer' }}>← {tUI('authBackToLogin', authLangue)}</button>
              </div>
            )
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
              {mode === 'signup' && wrapField(<User size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input placeholder={tUI('authNamePlaceholder', authLangue)} style={inputStyle} value={form.nom} onChange={set('nom')} />)}
              {wrapField(<Mail size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input placeholder={tUI('authEmailPlaceholder', authLangue)} style={inputStyle} value={form.email} onChange={set('email')} />)}
              {wrapField(<Lock size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input type="password" placeholder={tUI('authPasswordPlaceholder', authLangue)} style={inputStyle} value={form.password} onChange={set('password')} />)}
              {mode === 'signup' && wrapField(<Lock size={15} color={C.inkSoft} style={{ position: 'absolute', left: 12, top: 12 }} />, <input type="password" placeholder={tUI('authConfirmPasswordPlaceholder', authLangue)} style={inputStyle} value={form.confirm} onChange={set('confirm')} />)}

              {mode === 'login' && (
                <div style={{ textAlign: 'right' }}>
                  <button onClick={() => { setMode('forgot'); setError(''); }} style={{ background: 'none', border: 'none', color: ACCENTS.glacierDeep, fontSize: 12.5, fontWeight: 600, cursor: 'pointer' }}>{tUI('authForgotLink', authLangue)}</button>
                </div>
              )}

              {error && <div style={{ fontSize: 12.5, color: ACCENTS.red, background: ACCENTS.red + '12', borderRadius: 8, padding: '9px 11px' }}>{error}</div>}

              <button onClick={handleSubmit} disabled={loading} style={{ background: ACCENTS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '11px', fontSize: 14, fontWeight: 600, cursor: loading ? 'default' : 'pointer', marginTop: 4, opacity: loading ? 0.7 : 1 }}>
                {loading ? tUI('loadingWait', authLangue) : (mode === 'login' ? tUI('authSubmitLogin', authLangue) : tUI('authSubmitSignup', authLangue))}
              </button>
            </div>
          )}
        </div>
        <p style={{ textAlign: 'center', fontSize: 11.5, color: C.inkSoft, marginTop: 16 }}>{tUI('authPrototypeNote', authLangue)}</p>
      </div>
    </div>
  );
}"""

if old_auth in content:
    content = content.replace(old_auth, new_auth, 1)
    changes += 1
    print("OK - AuthScreen traduit")
else:
    print("ERREUR - AuthScreen non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes} modifications appliquees (Etape 10/N - AuthScreen).")
