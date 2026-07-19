import React from 'react';
import ReactDOM from 'react-dom/client';
import './lib/storage-shim.js'; // attache window.storage AVANT que l'app ne se monte
import App from './App.jsx';
import BookingPage from './BookingPage.jsx';

// Routage minimal sans dépendance externe :
// https://skipro-app.com/            -> l'app moniteur (App.jsx)
// https://skipro-app.com/<slug>      -> le formulaire public client (BookingPage.jsx)
//                                        <slug> = identifiant personnalisé choisi dans Paramètres (ex : /arthur)
const slug = window.location.pathname.replace(/^\/+|\/+$/g, '').toLowerCase();
const isBookingPage = slug.length > 0;

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {isBookingPage ? <BookingPage slug={slug} /> : <App />}
  </React.StrictMode>
);