import axios from "axios"

const api = axios.create({
  baseURL: "/api",
})

export const fetchBrands = () => api.get("/brands/")
export const fetchCategories = () => api.get("/categories/")
export const fetchProducts = () => api.get("/products/")
export const fetchCart = () => api.get("/cart/")
export const addToCart = (productId, quantity = 1) =>
  api.post("/cart/", { product_id: productId, quantity })
export const createOrder = (orderData) => api.post("/orders/create/", orderData)
