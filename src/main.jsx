import React from 'react';
import ReactDOM from 'react-dom/client';
import './lib/storage-shim.js'; // attache window.storage AVANT que l'app ne se monte
import App from './App.jsx';
import BookingPage from './BookingPage.jsx';

// Routage minimal sans dépendance externe :
// https://tonsite.com/           -> l'app moniteur (App.jsx)
// https://tonsite.com/reserver   -> le formulaire public client (BookingPage.jsx)
const isBookingPage = window.location.pathname.startsWith('/reserver');

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {isBookingPage ? <BookingPage /> : <App />}
  </React.StrictMode>
);
