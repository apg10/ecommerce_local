import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api";
import { useCart } from "../context/CartContext";

export default function ProductList() {
  const [products, setProducts] = useState([]);
  const { addItem } = useCart();

  useEffect(() => {
    api.get("/products")
      .then((res) => setProducts(res.data))
      .catch(console.error);
  }, []);

  const handleAdd = (p) => {
    addItem(p);
  };

  return (
    <div className="container">
      <h2>Products</h2>
      <div style={{ display: 'grid', gap: '1rem', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))' }}>
        {products.map((p) => (
          <div key={p.id} style={{ border: '1px solid #ddd', borderRadius: '4px', padding: '1rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            <Link to={"/product/" + p.id} style={{ textDecoration: 'none', color: 'inherit', flexGrow: 1 }}>
              <h3>{p.name}</h3>
              <p>{p.description}</p>
              <p>Price: {p.price}</p>
            </Link>
            <button onClick={() => handleAdd(p)} style={{ marginTop: '0.5rem' }}>Add to cart</button>
          </div>
        ))}
      </div>
    </div>
  );
}
