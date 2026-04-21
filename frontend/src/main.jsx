import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import { CartProvider } from './context/CartContext';
import './styles.css';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(
  <CartProvider>
    <App />
  </CartProvider>
);
