import React from "react";
import { useCart } from "../context/CartContext";

export default function Cart() {
  const { items, removeItem, clearCart } = useCart();

  const total = items.reduce((sum, i) => sum + i.price * i.quantity, 0);

  if (items.length === 0) return <div>Your cart is empty.</div>;

  return (
    <div>
      <h2>Your Cart</h2>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.name} x {item.quantity} = ${(item.price * item.quantity).toFixed(2)}
            <button onClick={() => removeItem(item.id)} style={{ marginLeft: '0.5rem' }}>Remove</button>
          </li>
        ))}
      </ul>
      <p>Total: ${total.toFixed(2)}</p>
      <button onClick={clearCart}>Clear Cart</button>
    </div>
  );
}
