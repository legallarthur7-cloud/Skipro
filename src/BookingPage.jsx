import React, { useState, useEffect, useMemo } from 'react';
import { Calendar, User, Send, CheckCircle2, Globe2 } from 'lucide-react';

const COLORS = {
  snow: '#FAFBFC', snowDim: '#F0F3F6', ice: '#E4EBF0', iceLine: '#D3DEE6',
  navy: '#10233D', ink: '#16232F', inkSoft: '#5A6B7A',
  glacier: '#2E6F8E', glacierDeep: '#1F5470', green: '#2F8F5B', blue: '#2E6F8E', amber: '#C99A46'
};

const STATIONS_BY_MASSIF = {
  'Alpes du Nord': [
    'Chamonix-Mont-Blanc', 'Megève', 'Saint-Gervais-les-Bains', 'Combloux', 'Les Contamines-Montjoie', 'Cordon', 'Les Houches',
    'Morzine', 'Avoriaz', 'Les Gets', 'Châtel', "Saint-Jean-d'Aulps",
    'La Clusaz', 'Le Grand-Bornand',
    'Flaine', 'Samoëns', "Les Carroz-d'Arâches", 'Sixt-Fer-à-Cheval',
    'Praz-sur-Arly', 'Notre-Dame-de-Bellecombe', 'Crest-Voland', 'Les Saisies', 'Hauteluce',
    'Courchevel', 'Méribel', 'Val Thorens', 'Les Menuires', 'Saint-Martin-de-Belleville', 'La Tania',
    'Tignes', "Val d'Isère", 'Les Arcs', 'La Plagne', 'Peisey-Vallandry', 'Champagny-en-Vanoise', 'Bourg-Saint-Maurice', 'Sainte-Foy-Tarentaise',
    'Valmorel', 'Saint-François-Longchamp', 'Valloire', 'Valfréjus', 'Aussois', 'Bonneval-sur-Arc', 'Val-Cenis', 'La Norma', 'Orelle',
    'Les Deux Alpes', "Alpe d'Huez", 'Chamrousse', 'Villard-de-Lans', 'Corrençon-en-Vercors', 'Autrans-Méaudre',
    "Le Collet d'Allevard", 'Les Sept Laux', 'Oz-en-Oisans', 'Vaujany', 'Auris-en-Oisans', 'La Grave'
  ],
  'Alpes du Sud': [
    'Serre Chevalier', 'Montgenèvre', 'Puy-Saint-Vincent', 'Vars', 'Risoul', 'Orcières-Merlette',
    'Superdévoluy', 'Ancelle', 'Pra-Loup', "La Foux d'Allos", 'Le Sauze', 'Auron', 'Isola 2000', 'Valberg', 'Gréolières-les-Neiges'
  ],
  'Pyrénées': [
    'La Pierre Saint-Martin', 'Gourette', 'Artouste', 'Le Somport',
    'Peyragudes', 'Piau-Engaly', 'Saint-Lary-Soulan', 'Luz-Ardiden', 'Barèges', 'La Mongie', 'Cauterets', 'Luchon-Superbagnères', 'Peyresourde',
    'Ax 3 Domaines', 'Ascou-Pailhères', 'Guzet', 'Le Mourtis',
    'Font-Romeu', 'Les Angles', 'Formiguères', 'Puyvalador', 'Porté-Puymorens', "Les Cambre d'Aze"
  ],
  'Jura': ['Les Rousses', 'Métabief', 'Mijoux-Monts Jura', 'Lélex', 'Chapelle-des-Bois'],
  'Vosges': ['La Bresse-Hohneck', 'Gérardmer', 'Le Markstein', 'Ventron', 'Lac Blanc-Orbey', 'Xonrupt-Longemer', 'Schnepfenried'],
  'Massif Central': ['Super Besse', 'Le Mont-Dore', 'Le Lioran', 'Chalmazel', 'La Bourboule', 'Chastreix-Sancy', 'Prat-de-Bouc'],
  'Corse': ['Ghisoni-Capannelle', "Val d'Ese", 'Haut Asco']
};
const STATIONS = Object.values(STATIONS_BY_MASSIF).flat();

const DISCIPLINES = ['Ski', 'Snowboard'];
const NIVEAUX = ['Débutant', 'Intermédiaire', 'Avancé', 'Expert'];
const ENGAGEMENTS = ['Heure', 'Demi-journée', 'Journée'];
// Purement informatif : le client indique juste sa préférence, aucun paiement n'est traité en
// ligne (voir paymentNote). Mêmes valeurs que côté moniteur (MODES_PAIEMENT dans App.jsx).
const MODES_PAIEMENT = ['Non renseigné', 'Espèces', 'Carte bancaire', 'Virement'];
const CRENEAUX_KEYS = ['Matin', 'Après-midi'];
const LANGUES_CANON = ['Français', 'Anglais', 'Allemand', 'Espagnol', 'Italien', 'Portugais', 'Russe'];

// Créneaux demi-journée : dépendent des horaires personnalisés du moniteur (Paramètres > Horaires),
// avec repli sur les valeurs par défaut si non renseignés.
function getCreneaux(settings) {
  return {
    'Matin': [settings.matinDebut || '09:00', settings.matinFin || '12:30'],
    'Après-midi': [settings.apresMidiDebut || '13:30', settings.apresMidiFin || '17:00']
  };
}

const DEFAULT_SETTINGS = {
  nom: 'Moniteur ESF', profession: 'Moniteur de ski indépendant', devise: 'EUR',
  matinDebut: '09:00', matinFin: '12:30', apresMidiDebut: '13:30', apresMidiFin: '17:00',
  tarifSkiHaute: 75, tarifSkiBasse: 55, tarifSnowboardHaute: 80, tarifSnowboardBasse: 60,
  tarifDemiJourneeHaute: 210, tarifDemiJourneeBasse: 150, tarifJourneeHaute: 370, tarifJourneeBasse: 270,
  seasonMode: 'vacances', zoneVacances: 'Toutes', hauteSaisonDebut: '12-20', hauteSaisonFin: '02-28'
};

const pad = (n) => String(n).padStart(2, '0');
const toKey = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
const monthDay = (dateKey) => dateKey.slice(5);
const fmtEUR = (n, devise = 'EUR') => new Intl.NumberFormat('fr-FR', { style: 'currency', currency: devise, maximumFractionDigits: 0 }).format(n || 0);
const timeToMinutes = (t) => { const [h, m] = t.split(':').map(Number); return h * 60 + m; };
const minutesToTime = (m) => `${pad(Math.floor(m / 60))}:${pad(m % 60)}`;

const HEURE_DURATION = 60; // durée par défaut d'un cours "Heure"
const DUREE_OPTIONS = [60, 90, 120]; // 1h, 1h30, 2h
const DUREE_LABELS = { 60: '1h', 90: '1h30', 120: '2h' };

// busySlots vient de l'API publique : uniquement { date, heureDebut, heureFin } des réservations non annulées.
const busyIntervals = (dateKey, busySlots) =>
  busySlots.filter(r => r.date === dateKey).map(r => [timeToMinutes(r.heureDebut), timeToMinutes(r.heureFin)]);

const overlaps = (start, end, intervals) => intervals.some(([s, e]) => start < e && end > s);

const availableHourStarts = (dateKey, busySlots, workStart, workEnd, duree = HEURE_DURATION) => {
  const busy = busyIntervals(dateKey, busySlots);
  const starts = [];
  for (let m = workStart; m + duree <= workEnd; m += 30) {
    if (!overlaps(m, m + duree, busy)) starts.push(m);
  }
  return starts;
};
const isCreneauFree = (dateKey, creneau, busySlots, creneaux) => {
  const busy = busyIntervals(dateKey, busySlots);
  const [s, e] = creneaux[creneau].map(timeToMinutes);
  return !overlaps(s, e, busy);
};
// Une "Journée" couvre toute la plage de travail du moniteur (matinDebut → apresMidiFin),
// pour correspondre exactement à ses horaires configurés (8h par défaut : 09:00–17:00).
const isJourneeFree = (dateKey, busySlots, workStart, workEnd) => {
  const busy = busyIntervals(dateKey, busySlots);
  return !overlaps(workStart, workEnd, busy);
};

const SCHOOL_HOLIDAYS = [
  { name: 'Toussaint', A: ['2025-10-18', '2025-11-03'], B: ['2025-10-18', '2025-11-03'], C: ['2025-10-18', '2025-11-03'] },
  { name: 'Noël', A: ['2025-12-20', '2026-01-05'], B: ['2025-12-20', '2026-01-05'], C: ['2025-12-20', '2026-01-05'] },
  { name: 'Hiver', A: ['2026-02-07', '2026-02-23'], B: ['2026-02-14', '2026-03-02'], C: ['2026-02-21', '2026-03-09'] },
  { name: 'Printemps', A: ['2026-04-04', '2026-04-20'], B: ['2026-04-11', '2026-04-27'], C: ['2026-04-18', '2026-05-04'] },
  { name: 'Été', A: ['2026-07-04', '2026-08-31'], B: ['2026-07-04', '2026-08-31'], C: ['2026-07-04', '2026-08-31'] },
  { name: 'Toussaint', A: ['2026-10-17', '2026-11-02'], B: ['2026-10-17', '2026-11-02'], C: ['2026-10-17', '2026-11-02'] },
  { name: 'Noël', A: ['2026-12-19', '2027-01-04'], B: ['2026-12-19', '2027-01-04'], C: ['2026-12-19', '2027-01-04'] },
  { name: 'Hiver', A: ['2027-02-13', '2027-03-01'], B: ['2027-02-20', '2027-03-08'], C: ['2027-02-06', '2027-02-22'] },
  { name: 'Printemps', A: ['2027-04-10', '2027-04-26'], B: ['2027-04-17', '2027-05-03'], C: ['2027-04-03', '2027-04-19'] },
  { name: 'Été', A: ['2027-07-03', '2027-08-31'], B: ['2027-07-03', '2027-08-31'], C: ['2027-07-03', '2027-08-31'] },
];
const inRange = (dateKey, [start, end]) => dateKey >= start && dateKey <= end;
// Les vacances d'Été sont exclues du calcul de haute saison (pas de saison de ski en juillet-août) —
// même logique que côté admin (App.jsx), pour que le client voie exactement le même prix que le moniteur.
const isSchoolHoliday = (dateKey, zone) => SCHOOL_HOLIDAYS.filter(p => p.name !== 'Été').some(p => zone === 'Toutes' ? (inRange(dateKey, p.A) || inRange(dateKey, p.B) || inRange(dateKey, p.C)) : inRange(dateKey, p[zone]));
const isHighSeason = (dateKey, settings) => {
  if (settings.seasonMode === 'manuel') {
    const md = monthDay(dateKey); const start = settings.hauteSaisonDebut, end = settings.hauteSaisonFin;
    if (!start || !end) return false;
    return start <= end ? (md >= start && md <= end) : (md >= start || md <= end);
  }
  return isSchoolHoliday(dateKey, settings.zoneVacances || 'Toutes');
};

/* ==================================================================================
   TRANSLATIONS
   ================================================================================== */
const UI_LANGS = [
  { code: 'fr', label: 'FR' }, { code: 'en', label: 'EN' }, { code: 'es', label: 'ES' },
  { code: 'de', label: 'DE' }, { code: 'it', label: 'IT' }, { code: 'pt', label: 'PT' }
];

const T = {
  fr: {
    title: 'Réserver un cours', subtitle: (nom) => `Remplis ce formulaire, ${nom} confirmera ta réservation rapidement.`,
    sectionInfo: 'Tes informations', sectionCourse: 'Ton cours',
    prenom: 'Prénom *', nom: 'Nom *', telephone: 'Téléphone *', email: 'E-mail', nationalite: 'Nationalité',
    langue: 'Langue parlée', age: 'Âge', nbPersonnes: 'Nombre de personnes',
    discipline: 'Discipline', niveau: 'Niveau', station: 'Station', date: 'Date souhaitée',
    priceLabel: (s) => `Tarif indicatif (${s})`, perHour: ' — par heure', heureLabel: 'Heure',
    message: 'Un message pour le moniteur ? (optionnel)', messagePh: 'Précisions, disponibilités, questions...',
    submit: 'Envoyer ma demande', submitting: 'Envoi en cours...',
    paymentNote: (nom) => `Le règlement se fait directement avec ${nom}, en espèces, carte ou virement — aucun paiement n'est demandé ici.`,
    errorRequired: 'Merci de renseigner au minimum ton prénom, nom, téléphone et la date souhaitée.',
    successTitle: 'Demande envoyée !', successBody: (prenom, nom) => `Merci ${prenom} ! Ta demande de cours a bien été transmise. ${nom} va la confirmer et te recontacter par téléphone ou e-mail.`,
    newRequest: 'Faire une nouvelle demande', high: 'haute saison', low: 'basse saison',
    notFoundTitle: 'Lien introuvable', notFoundBody: "Ce lien de réservation n'existe pas ou n'est plus actif.",
    loading: 'Chargement...',
    engagements: { 'Heure': 'Heure', 'Demi-journée': 'Demi-journée', 'Journée': 'Journée' },
    disciplines: { Ski: 'Ski', Snowboard: 'Snowboard' },
    niveaux: { Débutant: 'Débutant', Intermédiaire: 'Intermédiaire', Avancé: 'Avancé', Expert: 'Expert' },
    creneaux: { 'Matin': 'Matin', 'Après-midi': 'Après-midi' },
    langues: { Français: 'Français', Anglais: 'Anglais', Allemand: 'Allemand', Espagnol: 'Espagnol', Italien: 'Italien', Portugais: 'Portugais', Russe: 'Russe' },
    addCours: 'Ajouter ce cours', coursListTitle: 'Tes cours', removeCours: 'Retirer', totalLabel: 'Total',
    noCoursYet: 'Ajoute au moins un cours pour continuer.',
    heureDebutLabel: 'Heure de début', heureFinLabel: 'Heure de fin',
    heureRangeInvalidMsg: "L'heure de fin doit être après l'heure de début.",
    heureConflictMsg: 'Ce créneau chevauche une réservation déjà existante — merci de choisir un autre horaire.',
    heureOutsideHoursMsg: (start, end) => `En dehors des horaires habituels (${start}–${end}) — ta demande sera quand même envoyée, à valider par le moniteur.`,
    modePaiementLabel: 'Mode de paiement souhaité',
    modesPaiement: { 'Non renseigné': 'Pas de préférence', 'Espèces': 'Espèces', 'Carte bancaire': 'Carte bancaire', 'Virement': 'Virement' }
  },
  en: {
    title: 'Book a lesson', subtitle: (nom) => `Fill in this form and ${nom} will confirm your booking shortly.`,
    sectionInfo: 'Your details', sectionCourse: 'Your lesson',
    prenom: 'First name *', nom: 'Last name *', telephone: 'Phone *', email: 'E-mail', nationalite: 'Nationality',
    langue: 'Spoken language', age: 'Age', nbPersonnes: 'Number of people',
    discipline: 'Discipline', niveau: 'Level', station: 'Resort', date: 'Preferred date',
    priceLabel: (s) => `Estimated price (${s})`, perHour: ' — per hour', heureLabel: 'Time',
    message: 'A message for the instructor? (optional)', messagePh: 'Details, availability, questions...',
    submit: 'Send my request', submitting: 'Sending...',
    paymentNote: (nom) => `Payment is made directly with ${nom}, by cash, card or bank transfer — no payment is requested here.`,
    errorRequired: 'Please provide at least your first name, last name, phone number and preferred date.',
    successTitle: 'Request sent!', successBody: (prenom, nom) => `Thanks ${prenom}! Your lesson request has been sent. ${nom} will confirm it and get back to you by phone or e-mail.`,
    newRequest: 'Make a new request', high: 'high season', low: 'low season',
    notFoundTitle: 'Link not found', notFoundBody: 'This booking link does not exist or is no longer active.',
    loading: 'Loading...',
    engagements: { 'Heure': 'Hour', 'Demi-journée': 'Half-day', 'Journée': 'Full day' },
    disciplines: { Ski: 'Ski', Snowboard: 'Snowboard' },
    niveaux: { Débutant: 'Beginner', Intermédiaire: 'Intermediate', Avancé: 'Advanced', Expert: 'Expert' },
    creneaux: { 'Matin': 'Morning', 'Après-midi': 'Afternoon' },
    langues: { Français: 'French', Anglais: 'English', Allemand: 'German', Espagnol: 'Spanish', Italien: 'Italian', Portugais: 'Portuguese', Russe: 'Russian' },
    addCours: 'Add this lesson', coursListTitle: 'Your lessons', removeCours: 'Remove', totalLabel: 'Total',
    noCoursYet: 'Add at least one lesson to continue.',
    heureDebutLabel: 'Start time', heureFinLabel: 'End time',
    heureRangeInvalidMsg: 'The end time must be after the start time.',
    heureConflictMsg: 'This time slot overlaps an existing booking — please choose another time.',
    heureOutsideHoursMsg: (start, end) => `Outside usual hours (${start}–${end}) — your request will still be sent for the instructor to approve.`,
    modePaiementLabel: 'Preferred payment method',
    modesPaiement: { 'Non renseigné': 'No preference', 'Espèces': 'Cash', 'Carte bancaire': 'Card', 'Virement': 'Bank transfer' }
  },
  es: {
    title: 'Reservar una clase', subtitle: (nom) => `Rellena este formulario y ${nom} confirmará tu reserva enseguida.`,
    sectionInfo: 'Tus datos', sectionCourse: 'Tu clase',
    prenom: 'Nombre *', nom: 'Apellido *', telephone: 'Teléfono *', email: 'Correo electrónico', nationalite: 'Nacionalidad',
    langue: 'Idioma hablado', age: 'Edad', nbPersonnes: 'Número de personas',
    discipline: 'Disciplina', niveau: 'Nivel', station: 'Estación', date: 'Fecha deseada',
    priceLabel: (s) => `Precio orientativo (${s})`, perHour: ' — por hora', heureLabel: 'Hora',
    message: '¿Un mensaje para el monitor? (opcional)', messagePh: 'Detalles, disponibilidad, preguntas...',
    submit: 'Enviar mi solicitud', submitting: 'Enviando...',
    paymentNote: (nom) => `El pago se realiza directamente con ${nom}, en efectivo, tarjeta o transferencia — no se solicita ningún pago aquí.`,
    errorRequired: 'Por favor indica al menos tu nombre, apellido, teléfono y la fecha deseada.',
    successTitle: '¡Solicitud enviada!', successBody: (prenom, nom) => `¡Gracias ${prenom}! Tu solicitud de clase ha sido enviada. ${nom} la confirmará y se pondrá en contacto contigo por teléfono o correo.`,
    newRequest: 'Hacer una nueva solicitud', high: 'temporada alta', low: 'temporada baja',
    notFoundTitle: 'Enlace no encontrado', notFoundBody: 'Este enlace de reserva no existe o ya no está activo.',
    loading: 'Cargando...',
    engagements: { 'Heure': 'Hora', 'Demi-journée': 'Media jornada', 'Journée': 'Jornada completa' },
    disciplines: { Ski: 'Esquí', Snowboard: 'Snowboard' },
    niveaux: { Débutant: 'Principiante', Intermédiaire: 'Intermedio', Avancé: 'Avanzado', Expert: 'Experto' },
    creneaux: { 'Matin': 'Mañana', 'Après-midi': 'Tarde' },
    langues: { Français: 'Francés', Anglais: 'Inglés', Allemand: 'Alemán', Espagnol: 'Español', Italien: 'Italiano', Portugais: 'Portugués', Russe: 'Ruso' },
    addCours: 'Añadir esta clase', coursListTitle: 'Tus clases', removeCours: 'Quitar', totalLabel: 'Total',
    noCoursYet: 'Añade al menos una clase para continuar.',
    heureDebutLabel: 'Hora de inicio', heureFinLabel: 'Hora de fin',
    heureRangeInvalidMsg: 'La hora de fin debe ser posterior a la hora de inicio.',
    heureConflictMsg: 'Este horario se solapa con una reserva existente — elige otro horario.',
    heureOutsideHoursMsg: (start, end) => `Fuera del horario habitual (${start}–${end}) — tu solicitud se enviará igualmente para que el monitor la valide.`,
    modePaiementLabel: 'Método de pago preferido',
    modesPaiement: { 'Non renseigné': 'Sin preferencia', 'Espèces': 'Efectivo', 'Carte bancaire': 'Tarjeta', 'Virement': 'Transferencia' }
  },
  de: {
    title: 'Skikurs buchen', subtitle: (nom) => `Fülle dieses Formular aus, ${nom} bestätigt deine Buchung in Kürze.`,
    sectionInfo: 'Deine Angaben', sectionCourse: 'Dein Kurs',
    prenom: 'Vorname *', nom: 'Nachname *', telephone: 'Telefon *', email: 'E-Mail', nationalite: 'Nationalität',
    langue: 'Gesprochene Sprache', age: 'Alter', nbPersonnes: 'Anzahl Personen',
    discipline: 'Disziplin', niveau: 'Niveau', station: 'Skigebiet', date: 'Gewünschtes Datum',
    priceLabel: (s) => `Richtpreis (${s})`, perHour: ' — pro Stunde', heureLabel: 'Uhrzeit',
    message: 'Eine Nachricht an den Skilehrer? (optional)', messagePh: 'Details, Verfügbarkeit, Fragen...',
    submit: 'Anfrage senden', submitting: 'Wird gesendet...',
    paymentNote: (nom) => `Die Zahlung erfolgt direkt bei ${nom}, in bar, per Karte oder Überweisung — hier wird keine Zahlung verlangt.`,
    errorRequired: 'Bitte gib mindestens Vorname, Nachname, Telefonnummer und gewünschtes Datum an.',
    successTitle: 'Anfrage gesendet!', successBody: (prenom, nom) => `Danke ${prenom}! Deine Kursanfrage wurde übermittelt. ${nom} wird sie bestätigen und sich telefonisch oder per E-Mail bei dir melden.`,
    newRequest: 'Neue Anfrage stellen', high: 'Hochsaison', low: 'Nebensaison',
    notFoundTitle: 'Link nicht gefunden', notFoundBody: 'Dieser Buchungslink existiert nicht mehr oder ist nicht aktiv.',
    loading: 'Wird geladen...',
    engagements: { 'Heure': 'Stunde', 'Demi-journée': 'Halbtags', 'Journée': 'Ganztags' },
    disciplines: { Ski: 'Ski', Snowboard: 'Snowboard' },
    niveaux: { Débutant: 'Anfänger', Intermédiaire: 'Fortgeschritten', Avancé: 'Sehr fortgeschritten', Expert: 'Experte' },
    creneaux: { 'Matin': 'Vormittag', 'Après-midi': 'Nachmittag' },
    langues: { Français: 'Französisch', Anglais: 'Englisch', Allemand: 'Deutsch', Espagnol: 'Spanisch', Italien: 'Italienisch', Portugais: 'Portugiesisch', Russe: 'Russisch' },
    addCours: 'Diesen Kurs hinzufügen', coursListTitle: 'Deine Kurse', removeCours: 'Entfernen', totalLabel: 'Gesamt',
    noCoursYet: 'Füge mindestens einen Kurs hinzu, um fortzufahren.',
    heureDebutLabel: 'Startzeit', heureFinLabel: 'Endzeit',
    heureRangeInvalidMsg: 'Die Endzeit muss nach der Startzeit liegen.',
    heureConflictMsg: 'Diese Zeit überschneidet sich mit einer bestehenden Buchung — bitte wähle eine andere Zeit.',
    heureOutsideHoursMsg: (start, end) => `Außerhalb der üblichen Zeiten (${start}–${end}) — deine Anfrage wird trotzdem zur Bestätigung gesendet.`,
    modePaiementLabel: 'Bevorzugte Zahlungsart',
    modesPaiement: { 'Non renseigné': 'Keine Präferenz', 'Espèces': 'Bar', 'Carte bancaire': 'Karte', 'Virement': 'Überweisung' }
  },
  it: {
    title: 'Prenota una lezione', subtitle: (nom) => `Compila questo modulo, ${nom} confermerà la tua prenotazione a breve.`,
    sectionInfo: 'I tuoi dati', sectionCourse: 'La tua lezione',
    prenom: 'Nome *', nom: 'Cognome *', telephone: 'Telefono *', email: 'E-mail', nationalite: 'Nazionalità',
    langue: 'Lingua parlata', age: 'Età', nbPersonnes: 'Numero di persone',
    discipline: 'Disciplina', niveau: 'Livello', station: 'Stazione', date: 'Data desiderata',
    priceLabel: (s) => `Tariffa indicativa (${s})`, perHour: ' — all\'ora', heureLabel: 'Orario',
    message: 'Un messaggio per il maestro? (opzionale)', messagePh: 'Dettagli, disponibilità, domande...',
    submit: 'Invia la mia richiesta', submitting: 'Invio in corso...',
    paymentNote: (nom) => `Il pagamento avviene direttamente con ${nom}, in contanti, con carta o bonifico — nessun pagamento richiesto qui.`,
    errorRequired: 'Indica almeno nome, cognome, telefono e data desiderata.',
    successTitle: 'Richiesta inviata!', successBody: (prenom, nom) => `Grazie ${prenom}! La tua richiesta di lezione è stata inviata. ${nom} la confermerà e ti ricontatterà per telefono o e-mail.`,
    newRequest: 'Fai una nuova richiesta', high: 'alta stagione', low: 'bassa stagione',
    notFoundTitle: 'Link non trovato', notFoundBody: 'Questo link di prenotazione non esiste più o non è attivo.',
    loading: 'Caricamento...',
    engagements: { 'Heure': 'Ora', 'Demi-journée': 'Mezza giornata', 'Journée': 'Giornata intera' },
    disciplines: { Ski: 'Sci', Snowboard: 'Snowboard' },
    niveaux: { Débutant: 'Principiante', Intermédiaire: 'Intermedio', Avancé: 'Avanzato', Expert: 'Esperto' },
    creneaux: { 'Matin': 'Mattina', 'Après-midi': 'Pomeriggio' },
    langues: { Français: 'Francese', Anglais: 'Inglese', Allemand: 'Tedesco', Espagnol: 'Spagnolo', Italien: 'Italiano', Portugais: 'Portoghese', Russe: 'Russo' },
    addCours: 'Aggiungi questa lezione', coursListTitle: 'Le tue lezioni', removeCours: 'Rimuovi', totalLabel: 'Totale',
    noCoursYet: 'Aggiungi almeno una lezione per continuare.',
    heureDebutLabel: 'Ora di inizio', heureFinLabel: 'Ora di fine',
    heureRangeInvalidMsg: "L'orario di fine deve essere successivo all'orario di inizio.",
    heureConflictMsg: 'Questo orario si sovrappone a una prenotazione esistente — scegli un altro orario.',
    heureOutsideHoursMsg: (start, end) => `Fuori dagli orari abituali (${start}–${end}) — la tua richiesta verrà comunque inviata per l'approvazione del maestro.`,
    modePaiementLabel: 'Metodo di pagamento preferito',
    modesPaiement: { 'Non renseigné': 'Nessuna preferenza', 'Espèces': 'Contanti', 'Carte bancaire': 'Carta', 'Virement': 'Bonifico' }
  },
  pt: {
    title: 'Reservar uma aula', subtitle: (nom) => `Preenche este formulário e ${nom} confirmará a tua reserva em breve.`,
    sectionInfo: 'Os teus dados', sectionCourse: 'A tua aula',
    prenom: 'Nome *', nom: 'Apelido *', telephone: 'Telefone *', email: 'E-mail', nationalite: 'Nacionalidade',
    langue: 'Idioma falado', age: 'Idade', nbPersonnes: 'Número de pessoas',
    discipline: 'Modalidade', niveau: 'Nível', station: 'Estação', date: 'Data pretendida',
    priceLabel: (s) => `Preço indicativo (${s})`, perHour: ' — por hora', heureLabel: 'Hora',
    message: 'Uma mensagem para o monitor? (opcional)', messagePh: 'Detalhes, disponibilidade, perguntas...',
    submit: 'Enviar o meu pedido', submitting: 'A enviar...',
    paymentNote: (nom) => `O pagamento é feito diretamente com ${nom}, em dinheiro, cartão ou transferência — não é pedido nenhum pagamento aqui.`,
    errorRequired: 'Por favor indica pelo menos o teu nome, apelido, telefone e a data pretendida.',
    successTitle: 'Pedido enviado!', successBody: (prenom, nom) => `Obrigado ${prenom}! O teu pedido de aula foi enviado. ${nom} vai confirmá-lo e entrar em contacto por telefone ou e-mail.`,
    newRequest: 'Fazer um novo pedido', high: 'época alta', low: 'época baixa',
    notFoundTitle: 'Link não encontrado', notFoundBody: 'Este link de reserva não existe ou já não está ativo.',
    loading: 'A carregar...',
    engagements: { 'Heure': 'Hora', 'Demi-journée': 'Meio-dia', 'Journée': 'Dia inteiro' },
    disciplines: { Ski: 'Esqui', Snowboard: 'Snowboard' },
    niveaux: { Débutant: 'Iniciante', Intermédiaire: 'Intermédio', Avancé: 'Avançado', Expert: 'Especialista' },
    creneaux: { 'Matin': 'Manhã', 'Après-midi': 'Tarde' },
    langues: { Français: 'Francês', Anglais: 'Inglês', Allemand: 'Alemão', Espagnol: 'Espanhol', Italien: 'Italiano', Portugais: 'Português', Russe: 'Russo' },
    addCours: 'Adicionar esta aula', coursListTitle: 'As tuas aulas', removeCours: 'Remover', totalLabel: 'Total',
    noCoursYet: 'Adiciona pelo menos uma aula para continuar.',
    heureDebutLabel: 'Hora de início', heureFinLabel: 'Hora de fim',
    heureRangeInvalidMsg: 'A hora de fim deve ser depois da hora de início.',
    heureConflictMsg: 'Este horário sobrepõe-se a uma reserva já existente — escolhe outro horário.',
    heureOutsideHoursMsg: (start, end) => `Fora do horário habitual (${start}–${end}) — o teu pedido será enviado na mesma, para o monitor validar.`,
    modePaiementLabel: 'Método de pagamento preferido',
    modesPaiement: { 'Non renseigné': 'Sem preferência', 'Espèces': 'Dinheiro', 'Carte bancaire': 'Cartão', 'Virement': 'Transferência' }
  }
};

async function fetchPublicBooking(slug) {
  const res = await fetch(`/api/public-booking?slug=${encodeURIComponent(slug)}`);
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || 'Erreur inconnue');
  return data; // { userId, settings, busySlots }
}

async function postPublicBooking(slug, cours) {
  const res = await fetch('/api/public-booking', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ slug, cours })
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || 'Erreur inconnue');
  return data; // { ok, groupId, ids }
}

function computePrix(cours, settings) {
  const high = isHighSeason(cours.date, settings);
  if (cours.type === 'Journée') return high ? settings.tarifJourneeHaute : settings.tarifJourneeBasse;
  if (cours.type === 'Demi-journée') return high ? settings.tarifDemiJourneeHaute : settings.tarifDemiJourneeBasse;
  const hourlyRate = cours.discipline === 'Ski' ? (high ? settings.tarifSkiHaute : settings.tarifSkiBasse) : (high ? settings.tarifSnowboardHaute : settings.tarifSnowboardBasse);
  const duree = cours.duree || HEURE_DURATION;
  // Arrondi à l'euro supérieur, comme côté admin — le client voit le même montant que le moniteur.
  return Math.ceil(hourlyRate * (duree / 60));
}

const emptyForm = {
  prenom: '', nom: '', telephone: '', email: '', nationalite: '', langue: 'Français', age: '',
  nbPersonnes: 1, station: STATIONS[0], modePaiement: 'Non renseigné', message: ''
};

const emptyCoursDraft = {
  discipline: 'Ski', niveau: 'Débutant', date: toKey(new Date()), type: 'Heure', creneau: 'Matin',
  duree: HEURE_DURATION, heureDebut: '', heureFin: ''
};

export default function BookingPage({ slug }) {
  const [uiLang, setUiLang] = useState('fr');
  const [settings, setSettings] = useState(DEFAULT_SETTINGS);
  const [reservations, setReservations] = useState([]); // busySlots renvoyés par l'API publique
  const [form, setForm] = useState(emptyForm);
  const [coursDraft, setCoursDraft] = useState(emptyCoursDraft);
  const [coursList, setCoursList] = useState([]);
  const [sent, setSent] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [ready, setReady] = useState(false);
  const [notFound, setNotFound] = useState(false);
  const t = T[uiLang];

  useEffect(() => {
    const link = document.createElement('link');
    link.href = 'https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600;700&display=swap';
    link.rel = 'stylesheet'; document.head.appendChild(link);
    (async () => {
      try {
        const data = await fetchPublicBooking(slug);
        setSettings({ ...DEFAULT_SETTINGS, ...data.settings });
        setReservations(data.busySlots || []);
      } catch (e) {
        setNotFound(true);
      } finally {
        setReady(true);
      }
    })();
  }, [slug]);

  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }));
  const setDraft = (k) => (e) => setCoursDraft(d => ({ ...d, [k]: e.target.value }));

  // Créneaux occupés = ceux déjà réservés côté serveur + ceux déjà ajoutés à cette réservation multi-cours
  const combinedBusy = useMemo(() => {
    const staged = coursList.map(c => ({ date: c.date, heureDebut: c.heureDebut, heureFin: c.heureFin }));
    return [...reservations, ...staged];
  }, [reservations, coursList]);

  const high = isHighSeason(coursDraft.date, settings);
  const seasonLabel = high ? t.high : t.low;

  // Pré-remplit un horaire par défaut (raisonnable) dès que les horaires du moniteur sont chargés,
  // pour que les champs "Heure de début/fin" ne s'affichent pas vides au premier chargement —
  // le client reste ensuite entièrement libre de les modifier.
  useEffect(() => {
    if (!ready) return;
    setCoursDraft(d => (d.type === 'Heure' && !d.heureDebut && !d.heureFin)
      ? { ...d, heureDebut: settings.matinDebut || '09:00', heureFin: minutesToTime(timeToMinutes(settings.matinDebut || '09:00') + (d.duree || HEURE_DURATION)) }
      : d);
  }, [ready]); // eslint-disable-line react-hooks/exhaustive-deps

  const creneaux = useMemo(() => getCreneaux(settings), [settings]);
  const workStart = useMemo(() => timeToMinutes(settings.matinDebut || '09:00'), [settings]);
  const workEnd = useMemo(() => timeToMinutes(settings.apresMidiFin || '17:00'), [settings]);

  const matinFree = useMemo(() => isCreneauFree(coursDraft.date, 'Matin', combinedBusy, creneaux), [coursDraft.date, combinedBusy, creneaux]);
  const apremFree = useMemo(() => isCreneauFree(coursDraft.date, 'Après-midi', combinedBusy, creneaux), [coursDraft.date, combinedBusy, creneaux]);
  const journeeFree = useMemo(() => isJourneeFree(coursDraft.date, combinedBusy, workStart, workEnd), [coursDraft.date, combinedBusy, workStart, workEnd]);
  // Le type "Heure" n'est plus contraint à une liste de créneaux prédéfinis : le client choisit
  // librement son heure de début et de fin (voir heureConflict/heureRangeInvalid ci-dessous pour
  // la seule validation qui reste : la cohérence des heures et l'absence de chevauchement).
  const noAvailabilityAtAll = coursDraft.type !== 'Heure' && !matinFree && !apremFree && !journeeFree;

  const heureRangeInvalid = coursDraft.type === 'Heure' && !!coursDraft.heureDebut && !!coursDraft.heureFin && timeToMinutes(coursDraft.heureFin) <= timeToMinutes(coursDraft.heureDebut);
  const heureConflict = useMemo(() => {
    if (coursDraft.type !== 'Heure' || !coursDraft.heureDebut || !coursDraft.heureFin) return false;
    const s = timeToMinutes(coursDraft.heureDebut), e = timeToMinutes(coursDraft.heureFin);
    if (e <= s) return false;
    return overlaps(s, e, busyIntervals(coursDraft.date, combinedBusy));
  }, [coursDraft.type, coursDraft.date, coursDraft.heureDebut, coursDraft.heureFin, combinedBusy]);
  // Un cours "Heure" en dehors des horaires habituels du moniteur reste accepté : on informe
  // juste le client, la demande part quand même en "En attente" pour que le moniteur décide.
  const heureOutsideHours = coursDraft.type === 'Heure' && !!coursDraft.heureDebut && !!coursDraft.heureFin && !heureRangeInvalid &&
    (timeToMinutes(coursDraft.heureDebut) < workStart || timeToMinutes(coursDraft.heureFin) > workEnd);
  const derivedHeureDuree = useMemo(() => {
    if (coursDraft.type !== 'Heure' || !coursDraft.heureDebut || !coursDraft.heureFin) return coursDraft.duree || HEURE_DURATION;
    const d = timeToMinutes(coursDraft.heureFin) - timeToMinutes(coursDraft.heureDebut);
    return d > 0 ? d : (coursDraft.duree || HEURE_DURATION);
  }, [coursDraft.type, coursDraft.heureDebut, coursDraft.heureFin, coursDraft.duree]);
  const heureDraftInvalid = coursDraft.type === 'Heure' && (!coursDraft.heureDebut || !coursDraft.heureFin || heureRangeInvalid || heureConflict);

  // Corrige automatiquement la sélection si elle devient indisponible (changement de date, ajout d'un cours, etc.)
  // — ne s'applique plus au type "Heure", devenu totalement libre.
  useEffect(() => {
    setCoursDraft(d => {
      if (d.type === 'Demi-journée') {
        if (d.creneau === 'Matin' && !matinFree && apremFree) return { ...d, creneau: 'Après-midi', heureDebut: creneaux['Après-midi'][0], heureFin: creneaux['Après-midi'][1] };
        if (d.creneau === 'Après-midi' && !apremFree && matinFree) return { ...d, creneau: 'Matin', heureDebut: creneaux['Matin'][0], heureFin: creneaux['Matin'][1] };
      } else if (d.type === 'Journée' && !journeeFree) {
        return { ...d, type: 'Heure', heureDebut: d.heureDebut || minutesToTime(workStart), heureFin: d.heureFin || minutesToTime(workStart + (d.duree || HEURE_DURATION)) };
      }
      return d;
    });
  }, [coursDraft.date, combinedBusy]); // eslint-disable-line react-hooks/exhaustive-deps

  const draftEstimate = computePrix({ ...coursDraft, duree: derivedHeureDuree }, settings);

  const setType = (type) => {
    if (type === 'Journée' && !journeeFree) return;
    setCoursDraft(d => {
      if (type === 'Journée') return { ...d, type, heureDebut: minutesToTime(workStart), heureFin: minutesToTime(workEnd) };
      if (type === 'Demi-journée') {
        const cren = matinFree ? 'Matin' : (apremFree ? 'Après-midi' : (d.creneau || 'Matin'));
        return { ...d, type, creneau: cren, heureDebut: creneaux[cren][0], heureFin: creneaux[cren][1] };
      }
      const heureDebut = d.heureDebut || minutesToTime(workStart);
      const heureFin = (d.heureFin && timeToMinutes(d.heureFin) > timeToMinutes(heureDebut)) ? d.heureFin : minutesToTime(timeToMinutes(heureDebut) + (d.duree || HEURE_DURATION));
      return { ...d, type, heureDebut, heureFin };
    });
  };
  const setCreneau = (cren) => { if ((cren === 'Matin' && !matinFree) || (cren === 'Après-midi' && !apremFree)) return; setCoursDraft(d => ({ ...d, creneau: cren, heureDebut: creneaux[cren][0], heureFin: creneaux[cren][1] })); };
  // Heure de début/fin totalement libres (ex : 08:30→10:15) : le client tape directement l'horaire voulu.
  const setHeureDebutFree = (e) => {
    const heureDebut = e.target.value;
    setCoursDraft(d => {
      const keepFin = d.heureFin && timeToMinutes(d.heureFin) > timeToMinutes(heureDebut);
      return { ...d, heureDebut, heureFin: keepFin ? d.heureFin : minutesToTime(timeToMinutes(heureDebut) + (d.duree || HEURE_DURATION)) };
    });
  };
  const setHeureFinFree = (e) => setCoursDraft(d => ({ ...d, heureFin: e.target.value }));
  const setDuree = (mins) => {
    setCoursDraft(d => {
      const start = timeToMinutes(d.heureDebut || minutesToTime(workStart));
      return { ...d, duree: mins, heureDebut: d.heureDebut || minutesToTime(workStart), heureFin: minutesToTime(start + mins) };
    });
  };

  const addCours = () => {
    if (heureDraftInvalid) return;
    const heureDebut = coursDraft.heureDebut || creneaux['Matin'][0];
    const heureFin = coursDraft.heureFin || creneaux['Matin'][1];
    const prix = computePrix({ ...coursDraft, duree: derivedHeureDuree }, settings);
    setCoursList(list => [...list, { ...coursDraft, heureDebut, heureFin, duree: derivedHeureDuree, prix, uid: `${Date.now()}-${Math.random()}` }]);
    // Pour le type "Heure" (horaires libres), on enchaîne le prochain cours juste après celui
    // qu'on vient d'ajouter (même durée), plutôt que de vider les champs — ça évite au client
    // de devoir retaper un horaire à chaque cours supplémentaire lors d'une réservation multi-cours.
    if (coursDraft.type === 'Heure') {
      setCoursDraft(d => ({ ...d, heureDebut: heureFin, heureFin: minutesToTime(timeToMinutes(heureFin) + (derivedHeureDuree || HEURE_DURATION)) }));
    }
  };
  const removeCours = (uid) => setCoursList(list => list.filter(c => c.uid !== uid));

  const total = coursList.reduce((sum, c) => sum + (Number(c.prix) || 0), 0);

  const handleSubmit = async () => {
    if (!form.prenom || !form.nom || !form.telephone) { setError(t.errorRequired); return; }
    // Si le client n'a ajouté aucun cours à la liste (cas le plus fréquent : un seul cours),
    // on envoie directement le cours en cours de configuration — pas besoin de cliquer
    // "Ajouter ce cours" avant "Envoyer ma demande" quand il n'y en a qu'un seul.
    const draftUsable = coursDraft.type === 'Heure' ? !heureDraftInvalid : !noAvailabilityAtAll;
    const finalCoursList = coursList.length > 0 ? coursList : (draftUsable ? [{
      ...coursDraft,
      heureDebut: coursDraft.heureDebut || creneaux['Matin'][0],
      heureFin: coursDraft.heureFin || creneaux['Matin'][1],
      duree: derivedHeureDuree,
      prix: draftEstimate
    }] : []);
    if (finalCoursList.length === 0) { setError(t.noCoursYet); return; }
    setError(''); setLoading(true);
    const notes = form.message ? `Demande en ligne (${uiLang.toUpperCase()}) : ${form.message}` : `Demande envoyée via le formulaire en ligne (langue : ${uiLang.toUpperCase()}).`;
    const coursPayload = finalCoursList.map(c => ({
      nom: form.nom, prenom: form.prenom, telephone: form.telephone, email: form.email,
      nationalite: form.nationalite, langue: form.langue, age: Number(form.age) || '',
      niveau: c.niveau, discipline: c.discipline, nbPersonnes: Number(form.nbPersonnes) || 1, station: form.station,
      pointRdv: '', date: c.date, type: c.type, creneau: c.creneau, heureDebut: c.heureDebut, heureFin: c.heureFin,
      prix: c.prix, modePaiement: form.modePaiement || 'Non renseigné', notes
    }));
    try {
      await postPublicBooking(slug, coursPayload);
      setLoading(false);
      setSent(true);
    } catch (e) {
      setLoading(false);
      // Si un créneau vient d'être pris par quelqu'un d'autre, on rafraîchit les disponibilités affichées
      try { const fresh = await fetchPublicBooking(slug); setReservations(fresh.busySlots || []); } catch (_) { /* ignore */ }
      setError(e.message || "Une erreur est survenue lors de l'envoi. Merci de réessayer.");
    }
  };

  const inputStyle = { border: `1px solid ${COLORS.iceLine}`, borderRadius: 9, padding: '10px 12px', fontSize: 14.5, fontFamily: 'Inter, sans-serif', color: COLORS.ink, background: '#fff', width: '100%', boxSizing: 'border-box' };
  const field = (label, input) => <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}><label style={{ fontSize: 12.5, fontWeight: 600, color: COLORS.inkSoft }}>{label}</label>{input}</div>;

  const LangSwitcher = (
    <div style={{ display: 'flex', gap: 4, justifyContent: 'flex-end', marginBottom: 14 }}>
      {UI_LANGS.map(l => (
        <button key={l.code} onClick={() => setUiLang(l.code)} style={{
          padding: '5px 10px', borderRadius: 7, cursor: 'pointer', fontSize: 12, fontWeight: 700,
          border: `1px solid ${uiLang === l.code ? COLORS.glacier : COLORS.iceLine}`,
          background: uiLang === l.code ? COLORS.glacier : '#fff',
          color: uiLang === l.code ? '#fff' : COLORS.inkSoft
        }}>{l.label}</button>
      ))}
    </div>
  );

  if (!ready) {
    return (
      <div style={{ minHeight: '100vh', background: COLORS.snow, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: 'Inter, sans-serif', color: COLORS.inkSoft, fontSize: 14.5 }}>
        {t.loading}
      </div>
    );
  }

  if (notFound) {
    return (
      <div style={{ minHeight: '100vh', background: COLORS.snow, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 24, fontFamily: 'Inter, sans-serif' }}>
        <div style={{ maxWidth: 420, width: '100%', textAlign: 'center', background: '#fff', border: `1px solid ${COLORS.iceLine}`, borderRadius: 18, padding: '40px 32px' }}>
          <h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 21, fontWeight: 700, color: COLORS.navy, marginBottom: 10 }}>{t.notFoundTitle}</h1>
          <p style={{ fontSize: 14.5, color: COLORS.inkSoft, lineHeight: 1.6 }}>{t.notFoundBody}</p>
        </div>
      </div>
    );
  }

  if (sent) {
    return (
      <div style={{ minHeight: '100vh', background: COLORS.snow, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 24, fontFamily: 'Inter, sans-serif' }}>
        <div style={{ maxWidth: 440, width: '100%' }}>
          {LangSwitcher}
          <div style={{ textAlign: 'center', background: '#fff', border: `1px solid ${COLORS.iceLine}`, borderRadius: 18, padding: '40px 32px' }}>
            <div style={{ width: 52, height: 52, borderRadius: '50%', background: COLORS.green + '18', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 18px' }}>
              <CheckCircle2 size={26} color={COLORS.green} />
            </div>
            <h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 21, fontWeight: 700, color: COLORS.navy, marginBottom: 10 }}>{t.successTitle}</h1>
            <p style={{ fontSize: 14.5, color: COLORS.inkSoft, lineHeight: 1.6 }}>{t.successBody(form.prenom, settings.nom)}</p>
            <button onClick={() => { setForm(emptyForm); setCoursDraft(emptyCoursDraft); setCoursList([]); setSent(false); }} style={{ marginTop: 24, background: COLORS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '11px 22px', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}>{t.newRequest}</button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div style={{ minHeight: '100vh', background: COLORS.snow, fontFamily: 'Inter, sans-serif', color: COLORS.ink, padding: '32px 16px 60px' }}>
      <div style={{ maxWidth: 560, margin: '0 auto' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 9, fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 19, color: COLORS.navy }}>
            <span style={{ width: 20, height: 20, borderRadius: 5, background: `linear-gradient(135deg, ${COLORS.green} 33%, ${COLORS.blue} 33% 66%, #000 66%)` }} />
            SkiPro
          </div>
        </div>
        {LangSwitcher}
        <h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 26, fontWeight: 700, color: COLORS.navy, marginBottom: 8 }}>{t.title}</h1>
        <p style={{ fontSize: 14.5, color: COLORS.inkSoft, marginBottom: 28 }}>{t.subtitle(settings.nom)}</p>

        <div style={{ background: '#fff', border: `1px solid ${COLORS.iceLine}`, borderRadius: 16, padding: 24, display: 'flex', flexDirection: 'column', gap: 22 }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 13.5, fontWeight: 700, color: COLORS.navy, marginBottom: 14 }}><User size={15} /> {t.sectionInfo}</div>
            <div style={{ display: 'grid', gridTemplateColumns: 'minmax(0, 1fr) minmax(0, 1fr)', gap: 12 }}>
              {field(t.prenom, <input style={inputStyle} value={form.prenom} onChange={set('prenom')} />)}
              {field(t.nom, <input style={inputStyle} value={form.nom} onChange={set('nom')} />)}
              {field(t.telephone, <input style={inputStyle} value={form.telephone} onChange={set('telephone')} />)}
              {field(t.email, <input style={inputStyle} value={form.email} onChange={set('email')} />)}
              {field(t.nationalite, <input style={inputStyle} value={form.nationalite} onChange={set('nationalite')} />)}
              {field(t.langue, <select style={inputStyle} value={form.langue} onChange={set('langue')}>{LANGUES_CANON.map(l => <option key={l} value={l}>{t.langues[l]}</option>)}</select>)}
              {field(t.age, <input type="number" style={inputStyle} value={form.age} onChange={set('age')} />)}
              {field(t.nbPersonnes, <input type="number" min="1" style={inputStyle} value={form.nbPersonnes} onChange={set('nbPersonnes')} />)}
              {field(t.station, <select style={inputStyle} value={form.station} onChange={set('station')}>{Object.entries(STATIONS_BY_MASSIF).map(([massif, list]) => <optgroup key={massif} label={massif}>{list.map(s => <option key={s}>{s}</option>)}</optgroup>)}</select>)}
              {field(t.modePaiementLabel, <select style={inputStyle} value={form.modePaiement || 'Non renseigné'} onChange={set('modePaiement')}>{MODES_PAIEMENT.map(m => <option key={m} value={m}>{t.modesPaiement[m]}</option>)}</select>)}
            </div>
          </div>

          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 13.5, fontWeight: 700, color: COLORS.navy, marginBottom: 14 }}><Calendar size={15} /> {t.sectionCourse}</div>

            {coursList.length > 0 && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginBottom: 16 }}>
                <div style={{ fontSize: 12.5, fontWeight: 700, color: COLORS.inkSoft }}>{t.coursListTitle}</div>
                {coursList.map(c => (
                  <div key={c.uid} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: COLORS.snowDim, borderRadius: 9, padding: '9px 12px', gap: 8 }}>
                    <div style={{ fontSize: 12.5, color: COLORS.ink }}>
                      {c.date} · {t.disciplines[c.discipline]} · {t.engagements[c.type]} · {c.heureDebut}–{c.heureFin} — <strong>{fmtEUR(c.prix, settings.devise)}</strong>
                    </div>
                    <button type="button" onClick={() => removeCours(c.uid)} style={{ border: 'none', background: 'none', color: COLORS.amber, fontSize: 12, fontWeight: 600, cursor: 'pointer', whiteSpace: 'nowrap' }}>{t.removeCours}</button>
                  </div>
                ))}
              </div>
            )}

            <div style={{ display: 'grid', gridTemplateColumns: 'minmax(0, 1fr) minmax(0, 1fr)', gap: 12, marginBottom: 14 }}>
              {field(t.discipline, <select style={inputStyle} value={coursDraft.discipline} onChange={setDraft('discipline')}>{DISCIPLINES.map(d => <option key={d} value={d}>{t.disciplines[d]}</option>)}</select>)}
              {field(t.niveau, <select style={inputStyle} value={coursDraft.niveau} onChange={setDraft('niveau')}>{NIVEAUX.map(n => <option key={n} value={n}>{t.niveaux[n]}</option>)}</select>)}
              {field(t.date, <input type="date" style={inputStyle} value={coursDraft.date} onChange={setDraft('date')} />)}
            </div>
            <div style={{ display: 'flex', gap: 8, marginBottom: 10 }}>
              {ENGAGEMENTS.map(type => {
                const disabled = type === 'Journée' && !journeeFree;
                return (
                  <button key={type} type="button" disabled={disabled} onClick={() => setType(type)} style={{ flex: 1, padding: '9px 8px', borderRadius: 9, cursor: disabled ? 'not-allowed' : 'pointer', fontSize: 13, fontWeight: 600, border: `1px solid ${coursDraft.type === type ? COLORS.glacier : COLORS.iceLine}`, background: disabled ? COLORS.snowDim : (coursDraft.type === type ? COLORS.glacier + '18' : '#fff'), color: disabled ? COLORS.inkSoft : (coursDraft.type === type ? COLORS.glacierDeep : COLORS.ink), opacity: disabled ? 0.6 : 1 }}>{t.engagements[type]}</button>
                );
              })}
            </div>
            {coursDraft.type === 'Demi-journée' && (
              <div style={{ display: 'flex', gap: 8, marginBottom: 10 }}>
                {CRENEAUX_KEYS.map(cren => {
                  const free = cren === 'Matin' ? matinFree : apremFree;
                  return (
                    <button key={cren} type="button" disabled={!free} onClick={() => setCreneau(cren)} style={{ flex: 1, padding: '8px', borderRadius: 8, cursor: free ? 'pointer' : 'not-allowed', fontSize: 12.5, fontWeight: 600, border: `1px solid ${coursDraft.creneau === cren ? COLORS.glacier : COLORS.iceLine}`, background: !free ? COLORS.snowDim : (coursDraft.creneau === cren ? COLORS.glacier + '18' : '#fff'), color: !free ? COLORS.inkSoft : (coursDraft.creneau === cren ? COLORS.glacierDeep : COLORS.ink), opacity: free ? 1 : 0.6 }}>{t.creneaux[cren]} ({creneaux[cren][0]}–{creneaux[cren][1]}){!free ? ' 🚫' : ''}</button>
                  );
                })}
              </div>
            )}
            {coursDraft.type === 'Heure' && (
              <div style={{ display: 'flex', gap: 8, marginBottom: 10 }}>
                {DUREE_OPTIONS.map(mins => (
                  <button key={mins} type="button" onClick={() => setDuree(mins)} style={{ flex: 1, padding: '8px', borderRadius: 8, cursor: 'pointer', fontSize: 12.5, fontWeight: 600, border: `1px solid ${coursDraft.duree === mins ? COLORS.glacier : COLORS.iceLine}`, background: coursDraft.duree === mins ? COLORS.glacier + '18' : '#fff', color: coursDraft.duree === mins ? COLORS.glacierDeep : COLORS.ink }}>{DUREE_LABELS[mins]}</button>
                ))}
              </div>
            )}
            {coursDraft.type === 'Heure' && (
              <>
                <div style={{ display: 'grid', gridTemplateColumns: 'minmax(0, 1fr) minmax(0, 1fr)', gap: 12, marginBottom: 10 }}>
                  {field(t.heureDebutLabel, <input type="time" style={inputStyle} value={coursDraft.heureDebut || ''} onChange={setHeureDebutFree} />)}
                  {field(t.heureFinLabel, <input type="time" style={inputStyle} value={coursDraft.heureFin || ''} onChange={setHeureFinFree} />)}
                </div>
                {heureRangeInvalid && (
                  <div style={{ fontSize: 12.5, color: COLORS.amber, background: COLORS.amber + '15', borderRadius: 8, padding: '9px 11px', marginBottom: 10 }}>{t.heureRangeInvalidMsg}</div>
                )}
                {!heureRangeInvalid && heureConflict && (
                  <div style={{ fontSize: 12.5, color: COLORS.amber, background: COLORS.amber + '15', borderRadius: 8, padding: '9px 11px', marginBottom: 10 }}>{t.heureConflictMsg}</div>
                )}
                {!heureRangeInvalid && !heureConflict && heureOutsideHours && (
                  <div style={{ fontSize: 12.5, color: COLORS.glacierDeep, background: COLORS.glacier + '15', borderRadius: 8, padding: '9px 11px', marginBottom: 10 }}>{t.heureOutsideHoursMsg(settings.matinDebut || '09:00', settings.apresMidiFin || '17:00')}</div>
                )}
              </>
            )}
            {noAvailabilityAtAll && (
              <div style={{ fontSize: 12.5, color: COLORS.amber, background: COLORS.amber + '15', borderRadius: 8, padding: '9px 11px', marginBottom: 10 }}>
                Cette date est complète, quel que soit le format de cours. Merci de choisir une autre date.
              </div>
            )}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: COLORS.snowDim, borderRadius: 9, padding: '10px 14px', marginBottom: 12 }}>
              <span style={{ fontSize: 12.5, color: COLORS.inkSoft }}>{t.priceLabel(seasonLabel)}{coursDraft.type === 'Heure' ? t.perHour : ''}</span>
              <span style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 16, color: COLORS.navy }}>{fmtEUR(draftEstimate, settings.devise)}</span>
            </div>
            <button type="button" onClick={addCours} disabled={coursDraft.type === 'Heure' ? heureDraftInvalid : noAvailabilityAtAll} style={{ width: '100%', padding: '10px', borderRadius: 9, border: `1px dashed ${COLORS.glacier}`, background: '#fff', color: COLORS.glacierDeep, fontSize: 13, fontWeight: 600, cursor: (coursDraft.type === 'Heure' ? heureDraftInvalid : noAvailabilityAtAll) ? 'not-allowed' : 'pointer', opacity: (coursDraft.type === 'Heure' ? heureDraftInvalid : noAvailabilityAtAll) ? 0.6 : 1 }}>+ {t.addCours}</button>

            {coursList.length > 0 && (
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 16, paddingTop: 14, borderTop: `1px solid ${COLORS.iceLine}` }}>
                <span style={{ fontSize: 13.5, fontWeight: 700, color: COLORS.navy }}>{t.totalLabel}</span>
                <span style={{ fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 18, color: COLORS.navy }}>{fmtEUR(total, settings.devise)}</span>
              </div>
            )}
          </div>

          {field(t.message, <textarea style={{ ...inputStyle, minHeight: 70, resize: 'vertical' }} value={form.message} onChange={set('message')} placeholder={t.messagePh} />)}

          {error && <div style={{ fontSize: 13, color: COLORS.amber, background: COLORS.amber + '15', borderRadius: 8, padding: '10px 12px' }}>{error}</div>}

          <button onClick={handleSubmit} disabled={loading || (coursList.length === 0 && (coursDraft.type === 'Heure' ? heureDraftInvalid : noAvailabilityAtAll))} style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, background: COLORS.glacier, color: '#fff', border: 'none', borderRadius: 9, padding: '13px', fontSize: 14.5, fontWeight: 600, cursor: (loading || (coursList.length === 0 && (coursDraft.type === 'Heure' ? heureDraftInvalid : noAvailabilityAtAll))) ? 'default' : 'pointer', opacity: (loading || (coursList.length === 0 && (coursDraft.type === 'Heure' ? heureDraftInvalid : noAvailabilityAtAll))) ? 0.6 : 1 }}>
            <Send size={16} /> {loading ? t.submitting : t.submit}
          </button>
          <p style={{ fontSize: 11.5, color: COLORS.inkSoft, textAlign: 'center' }}>{t.paymentNote(settings.nom)}</p>
        </div>
        {/* Pied de page légal : liens obligatoires visibles par les clients (RGPD, LCEN). */}
        <div style={{ display: 'flex', justifyContent: 'center', gap: 14, flexWrap: 'wrap', marginTop: 24, fontSize: 11.5 }}>
          <a href="/legal/mentions" style={{ color: COLORS.inkSoft, textDecoration: 'none' }}>Mentions légales</a>
          <a href="/legal/confidentialite" style={{ color: COLORS.inkSoft, textDecoration: 'none' }}>Confidentialité</a>
          <a href="/legal/cgu" style={{ color: COLORS.inkSoft, textDecoration: 'none' }}>CGU</a>
          <a href="/legal/cgv" style={{ color: COLORS.inkSoft, textDecoration: 'none' }}>CGV</a>
        </div>
      </div>
    </div>
  );
}
