import React from 'react';
import { Link } from 'react-router-dom';

function NavBar() {
  return (
    <nav style={{ padding: '1rem', background: '#f8f8f8' }}>
      <Link to="/" style={{ marginRight: '1rem' }}>Home</Link>
      <Link to="/products" style={{ marginRight: '1rem' }}>Products</Link>
      <Link to="/cart">Cart</Link>
    </nav>
  );
}
export default NavBar;
