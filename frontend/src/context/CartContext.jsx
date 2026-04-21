import { createContext, useState, useContext, useEffect } from 'react';
import api from '../api';

const CartContext = createContext();

export function CartProvider({ children }) {
  const [items, setItems] = useState([]);

  // Load cart from backend on mount
  useEffect(() => {
    api.get('/cart')
      .then(res => setItems(res.data.items || []))
      .catch(err => console.error('Cart load error', err));
  }, []);

  const addItem = (product) => {
    setItems(prev => {
      const existing = prev.find(i => i.id === product.id);
      if (existing) {
        return prev.map(i =>
          i.id === product.id ? { ...i, quantity: i.quantity + (product.quantity || 1) } : i
        );
      }
      return [...prev, { ...product, quantity: product.quantity || 1 }];
    });
    api.post('/cart', {
      product_id: product.id,
      quantity: product.quantity || 1,
    }).catch(err => console.error('Add to cart failed', err));
  };

  const removeItem = (id) => {
    setItems(prev => prev.filter(i => i.id !== id));
    // Optional: sync removal to backend
  };

  const clearCart = () => {
    setItems([]);
    // No backend sync
  };

  return (
    <CartContext.Provider value={{ items, addItem, removeItem, clearCart }}>
      {children}
    </CartContext.Provider>
  );
}

export const useCart = () => useContext(CartContext);

