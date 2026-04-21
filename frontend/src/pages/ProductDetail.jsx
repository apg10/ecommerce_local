import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api";
import { useCart } from "../context/CartContext";

export default function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const { addItem } = useCart();

  useEffect(() => {
    api.get(`/products/${id}`)
      .then((res) => setProduct(res.data))
      .catch(console.error);
  }, [id]);

  if (!product) return <div>Loading...</div>;

  const [qty, setQty] = useState(1);
  const handleAdd = () => addItem({ ...product, quantity: qty });

  return (
    <div className="product-detail">
      <h2>{product.name}</h2>
      {product.image_url && (
        <img src={product.image_url} alt={product.name} className="product-image" />
      )}
      <p>{product.description}</p>
      <p className="price">Price: {product.price}</p>
      <div style={{ display: 'flex', alignItems: 'center', marginTop: '0.5rem' }}>
        <label htmlFor="qty">Qty:</label>
        <input
          id="qty"
          type="number"
          min="1"
          value={qty}
          onChange={(e) => setQty(parseInt(e.target.value) || 1)}
          style={{ width: '60px', marginLeft: '0.5rem' }}
        />
        <button onClick={handleAdd} style={{ marginLeft: '1rem' }}>
          Add to cart
        </button>
      </div>
    </div>
  );
}
