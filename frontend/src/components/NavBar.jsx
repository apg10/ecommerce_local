import React from "react";
import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";

function NavBar() {
  const { items } = useCart();
  const total = items.reduce((sum, i) => sum + i.quantity, 0);

  return (
    <nav style={{ padding: "1rem", background: "#f8f8f8", display: "flex", gap: "1rem" }}>
      <Link to="/" style={{ marginRight: "1rem" }}>Home</Link>
      <Link to="/products" style={{ marginRight: "1rem" }}>Products</Link>
      <Link to="/cart">Cart ({total})</Link>
      <Link to="/checkout" style={{ marginLeft: "auto" }}>Checkout</Link>
    </nav>
  );
}

export default NavBar;
