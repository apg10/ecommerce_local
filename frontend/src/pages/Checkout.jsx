import React, { useState } from "react";
import { useCart } from "../context/CartContext";
import { useNavigate } from "react-router-dom";

export default function Checkout() {
  const { items, clearCart } = useCart();
  const navigate = useNavigate();

  const [form, setForm] = useState({
    name: "",
    email: "",
    address: "",
    city: "",
    zip: "",
  });

  const total = items.reduce((sum, i) => sum + i.price * i.quantity, 0);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // For demo: simply log and clear cart
    console.log("Checkout data:", { form, items });
    clearCart();
    navigate("/");
  };

  return (
    <div className="container">
      <h2>Checkout</h2>
      <p>Order total: ${total.toFixed(2)}</p>
      <form onSubmit={handleSubmit} style={{ display: 'grid', gap: '0.5rem', maxWidth: '400px' }}>
        <label>
          Name
          <input name="name" value={form.name} onChange={handleChange} required />
        </label>
        <label>
          Email
          <input name="email" type="email" value={form.email} onChange={handleChange} required />
        </label>
        <label>
          Address
          <input name="address" value={form.address} onChange={handleChange} required />
        </label>
        <label>
          City
          <input name="city" value={form.city} onChange={handleChange} required />
        </label>
        <label>
          ZIP
          <input name="zip" value={form.zip} onChange={handleChange} required />
        </label>
        <button type="submit">Place Order</button>
      </form>
    </div>
  );
}
