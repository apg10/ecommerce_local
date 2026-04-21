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
    <div>
      <h2>Products</h2>
      <ul>
        {products.map((p) => (
          <li key={p.id}>
            <Link to={"/product/" + p.id}>{p.name}</Link>
            <button onClick={() => handleAdd(p)}>Add to cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
