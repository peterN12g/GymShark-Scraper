import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { checkPermission, registerSW, requestNotificationPermission } from './sw-dependencies';

try {
  checkPermission();
  registerSW();
  requestNotificationPermission();
} catch (e) {
  console.log(e)
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);



reportWebVitals();
