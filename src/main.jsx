import React from 'react';
import ReactDOM from 'react-dom/client';
import './lib/storage-shim.js'; // attache window.storage AVANT que l'app ne se monte
import App from './App.jsx';
import BookingPage from './BookingPage.jsx';
import LegalPage from './LegalPage.jsx';

// Routage minimal sans dépendance externe :
// https://skipro-app.com/             -> l'app moniteur (App.jsx)
// https://skipro-app.com/legal        -> pages légales (mentions, confidentialité, CGU, CGV)
// https://skipro-app.com/legal/cgu    -> pages légales, ouvertes sur un document précis
// https://skipro-app.com/<slug>       -> le formulaire public client (BookingPage.jsx)
//                                         <slug> = identifiant personnalisé choisi dans Paramètres (ex : /arthur)
const path = window.location.pathname.replace(/^\/+|\/+$/g, '').toLowerCase();
const parts = path.split('/');
// "legal" est un chemin réservé (non attribuable comme slug de moniteur).
const isLegalPage = parts[0] === 'legal';
const slug = path;
const isBookingPage = !isLegalPage && slug.length > 0;

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {isLegalPage ? <LegalPage initialTab={parts[1]} /> : isBookingPage ? <BookingPage slug={slug} /> : <App />}
  </React.StrictMode>
);
