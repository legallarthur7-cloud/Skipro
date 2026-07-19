with open('src/App.jsx', 'r') as f:
    content = f.read()

changes = 0
total = 9

# 1. Ajouter la fonction utilitaire fmtHeure juste apres LOCALE_MAP/DAYS_SHORT_MAP
old_anchor = """const DAYS_SHORT_MAP = {
  Français: ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'],
  Anglais: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  Espagnol: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'],
  Italien: ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'],
  Portugais: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
};"""

new_anchor = """const DAYS_SHORT_MAP = {
  Français: ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'],
  Anglais: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  Espagnol: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'],
  Italien: ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'],
  Portugais: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
};
function fmtHeure(hhmm, langue) {
  if (langue !== 'Anglais' || !hhmm || !hhmm.includes(':')) return hhmm;
  const [hStr, mStr] = hhmm.split(':');
  let h = parseInt(hStr, 10);
  const period = h >= 12 ? 'PM' : 'AM';
  h = h % 12; if (h === 0) h = 12;
  return `${h}:${mStr} ${period}`;
}"""

if old_anchor in content:
    content = content.replace(old_anchor, new_anchor, 1)
    changes += 1
    print("OK 1/9 - Fonction fmtHeure ajoutee")
else:
    print("ERREUR 1/9 - Ancre DAYS_SHORT_MAP non trouvee")

# 2. CalendarView - heures de la colonne de gauche (gutter)
old_gutter = """<div style={{ width: 52, flexShrink: 0 }}>{hours.map(h => <div key={h} style={{ height: ROW_HEIGHT, fontSize: 11, color: C.inkSoft, textAlign: 'right', paddingRight: 8, position: 'relative', top: -6 }}>{pad(h)}:00</div>)}</div>"""
new_gutter = """<div style={{ width: 52, flexShrink: 0 }}>{hours.map(h => <div key={h} style={{ height: ROW_HEIGHT, fontSize: 11, color: C.inkSoft, textAlign: 'right', paddingRight: 8, position: 'relative', top: -6 }}>{fmtHeure(`${pad(h)}:00`, langue)}</div>)}</div>"""

if old_gutter in content:
    content = content.replace(old_gutter, new_gutter, 1)
    changes += 1
    print("OK 2/9 - Heures colonne gauche du calendrier converties")
else:
    print("ERREUR 2/9 - Gutter horaire non trouve")

# 3. CalendarView - heures affichees sur les evenements du calendrier
old_event = """<div style={{ fontSize: 10.5, color: C.inkSoft }}>{ev.heureDebut}–{ev.heureFin}</div>"""
new_event = """<div style={{ fontSize: 10.5, color: C.inkSoft }}>{fmtHeure(ev.heureDebut, langue)}–{fmtHeure(ev.heureFin, langue)}</div>"""

if old_event in content:
    content = content.replace(old_event, new_event, 1)
    changes += 1
    print("OK 3/9 - Heures des evenements du calendrier converties")
else:
    print("ERREUR 3/9 - Bloc evenement calendrier non trouve")

# 4. Dashboard - liste des prochains cours
old_dash_upcoming = """<div><div style={{ fontSize: 13.5, fontWeight: 600, color: C.ink }}>{r.prenom} {r.nom}</div><div style={{ fontSize: 12.5, color: C.inkSoft }}>{fmtDateShort(r.date)} · {r.heureDebut} · {r.station}</div></div>"""
new_dash_upcoming = """<div><div style={{ fontSize: 13.5, fontWeight: 600, color: C.ink }}>{r.prenom} {r.nom}</div><div style={{ fontSize: 12.5, color: C.inkSoft }}>{fmtDateShort(r.date)} · {fmtHeure(r.heureDebut, langue)} · {r.station}</div></div>"""

if old_dash_upcoming in content:
    content = content.replace(old_dash_upcoming, new_dash_upcoming, 1)
    changes += 1
    print("OK 4/9 - Heures Dashboard (prochains cours) converties")
else:
    print("ERREUR 4/9 - Bloc Dashboard prochains cours non trouve")

# 5. ReservationsView - tableau
old_res_table = """<td style={td}>{r.prenom} {r.nom}</td><td style={td}>{fmtDateShort(r.date)}</td><td style={td}>{r.heureDebut}–{r.heureFin}</td>"""
new_res_table = """<td style={td}>{r.prenom} {r.nom}</td><td style={td}>{fmtDateShort(r.date)}</td><td style={td}>{fmtHeure(r.heureDebut, langue)}–{fmtHeure(r.heureFin, langue)}</td>"""

if old_res_table in content:
    content = content.replace(old_res_table, new_res_table, 1)
    changes += 1
    print("OK 5/9 - Heures tableau Reservations converties")
else:
    print("ERREUR 5/9 - Tableau Reservations non trouve")

# 6. ReservationModal - boutons de creneau (Matin/Apres-midi avec horaires)
old_creneau_btn = """}}>{creneauLabel(cren)} ({CRENEAUX[cren][0]}–{CRENEAUX[cren][1]})</button>"""
new_creneau_btn = """}}>{creneauLabel(cren)} ({fmtHeure(CRENEAUX[cren][0], langue)}–{fmtHeure(CRENEAUX[cren][1], langue)})</button>"""

if old_creneau_btn in content:
    content = content.replace(old_creneau_btn, new_creneau_btn, 1)
    changes += 1
    print("OK 6/9 - Boutons creneau du formulaire de reservation convertis")
else:
    print("ERREUR 6/9 - Boutons creneau non trouves")

# 7. InvoiceModal - ajouter langue + convertir les heures dans la description
old_invoice_langue = """function InvoiceModal({ reservation, onClose, C, devise, settings }) {
  const invoiceNumber = `${String(reservation.id).slice(-6)}${new Date(reservation.date).getFullYear()}`;
  const todayStr = new Date().toLocaleDateString('fr-FR');
  const hasBank = settings.iban || settings.bic || settings.banque;"""
new_invoice_langue = """function InvoiceModal({ reservation, onClose, C, devise, settings }) {
  const langue = settings.langue;
  const invoiceNumber = `${String(reservation.id).slice(-6)}${new Date(reservation.date).getFullYear()}`;
  const todayStr = new Date().toLocaleDateString('fr-FR');
  const hasBank = settings.iban || settings.bic || settings.banque;"""

if old_invoice_langue in content:
    content = content.replace(old_invoice_langue, new_invoice_langue, 1)
    changes += 1
    print("OK 7/9 - Variable langue ajoutee dans InvoiceModal")
else:
    print("ERREUR 7/9 - Debut InvoiceModal non trouve")

old_invoice_time = """Cours de {reservation.discipline.toLowerCase()} à {reservation.station || ''} — {fmtDateShort(reservation.date)} ({reservation.heureDebut}–{reservation.heureFin})"""
new_invoice_time = """Cours de {reservation.discipline.toLowerCase()} à {reservation.station || ''} — {fmtDateShort(reservation.date)} ({fmtHeure(reservation.heureDebut, langue)}–{fmtHeure(reservation.heureFin, langue)})"""

if old_invoice_time in content:
    content = content.replace(old_invoice_time, new_invoice_time, 1)
    changes += 1
    print("OK 8/9 - Heures de la facture converties")
else:
    print("ERREUR 8/9 - Ligne description facture non trouvee")

# 8. ClientModal - historique des cours
old_client_history = """<div><div style={{ fontSize: 13, fontWeight: 600, color: C.ink }}>{fmtDateShort(r.date)} · {r.heureDebut}–{r.heureFin}</div><div style={{ fontSize: 12, color: C.inkSoft }}>{r.station} · {r.niveau}</div></div>"""
new_client_history = """<div><div style={{ fontSize: 13, fontWeight: 600, color: C.ink }}>{fmtDateShort(r.date)} · {fmtHeure(r.heureDebut, langue)}–{fmtHeure(r.heureFin, langue)}</div><div style={{ fontSize: 12, color: C.inkSoft }}>{r.station} · {r.niveau}</div></div>"""

if old_client_history in content:
    content = content.replace(old_client_history, new_client_history, 1)
    changes += 1
    print("OK 9/9 - Heures historique client converties")
else:
    print("ERREUR 9/9 - Historique client non trouve")

with open('src/App.jsx', 'w') as f:
    f.write(content)

print(f"\n{changes}/{total} modifications appliquees (Chantier special - format horaire 12h anglais).")
