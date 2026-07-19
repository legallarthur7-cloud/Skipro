with open('src/App.jsx', 'r') as f:
    content = f.read()

old = """  const handleSubscribe = async () => {
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
  };"""

new = """  const handleSubscribe = async () => {
    setSubLoading(true);
    try {
      const { data: { user } } = await supabase.auth.getUser();
      const res = await fetch('/api/create-checkout-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: form.email, telephone: form.telephone || '', userId: user?.id || '' }),
      });
      const data = await res.json();
      if (data.url) window.location.href = data.url;
      else { alert('Erreur : ' + (data.error || 'inconnue')); setSubLoading(false); }
    } catch (e) {
      alert('Erreur de connexion à Stripe.');
      setSubLoading(false);
    }
  };"""

if old in content:
    content = content.replace(old, new, 1)
    print("OK - handleSubscribe mis a jour (telephone + userId envoyes)")
else:
    print("ERREUR - handleSubscribe non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)
