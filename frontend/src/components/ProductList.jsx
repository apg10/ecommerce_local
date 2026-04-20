import { useEffect, useState } from "react"
import { fetchProducts } from "../api"

const ProductList = () => {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)
  useEffect(() => {
    fetchProducts()
      .then((res) => setProducts(res.data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [])
  if (loading) return <div>Loading...</div>
  return (
    <div>
      <h2>Products</h2>
      <ul>
        {products.map((p) => (
          <li key={p.id}>
            {p.name} – {p.price}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default ProductList
