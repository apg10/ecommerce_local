import React, { useEffect, useState } from "react";
import api from "../api";

export default function ProductList() {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    api.get("/products")
      .then((res) => setProducts(res.data))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Products</h2>
      <ul>
        {products.map((p) => (
          <li key={p.id}>
            <a href={"/product/" + p.id}>{p.name}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}
