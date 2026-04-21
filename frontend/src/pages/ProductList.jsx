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
      <div className="product-grid">
        {products.map((p) => (
          <div key={p.id} className="product-card">
            <Link to={"/product/" + p.id} className="card-link">
              {p.image_url && (
                <img src={p.image_url} alt={p.name} className="product-image" />
              )}
              <h3>{p.name}</h3>
              <p>{p.description}</p>
              <p className="price">Price: {p.price}</p>
            </Link>
            <button onClick={() => handleAdd(p)} className="add-btn">
              Add to cart
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
