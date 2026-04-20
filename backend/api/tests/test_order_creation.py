"""High‑value tests for order creation and cart‑to‑order workflow.

These tests focus on business logic that could impact revenue or data integrity:
* Adding items to the cart respects stock limits.
* Creating an order correctly transfers cart items and calculates totals.
* Orders cannot be created with an empty cart.
* Guest users receive a provisional customer profile.
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from core import models
from core.models import Product, Category, Brand, CartItem, Order, OrderItem
from django.urls import reverse

User = get_user_model()


class OrderCreationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(name="OBrand")
        self.category = Category.objects.create(name="OCat")
        self.product = Product.objects.create(
            name="OProduct", brand=self.brand, category=self.category, price=25.00, stock=3
        )
        self.user = User.objects.create_user(username="orduser", password="pw")

    def _add_to_cart(self, qty, user=None):
        url = reverse("cart")
        payload = {"product_id": self.product.id, "quantity": qty}
        if user:
            self.client.login(username=user.username, password="pw")
        return self.client.post(url, payload)

    def test_cart_to_order_flow_authenticated(self):
        # Add items to cart
        resp = self._add_to_cart(2, user=self.user)
        self.assertEqual(resp.status_code, 200)
        # Create order
        url = reverse("order-create")
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 201)
        data = resp.json()
        self.assertEqual(data["status"], "created")
        self.assertEqual(data["total"], "50.00")  # 2 * 25.00
        # Order items created
        order = Order.objects.get(id=data["id"])
        self.assertEqual(order.items.count(), 1)
        item = order.items.first()
        self.assertEqual(item.quantity, 2)
        self.assertEqual(item.product, self.product)
        # Cart should be empty after order
        cart = models.Cart.objects.get(customer=order.customer)
        self.assertEqual(cart.items.count(), 0)

    def test_cart_to_order_flow_guest(self):
        # Guest user adds to cart
        resp = self._add_to_cart(1)
        self.assertEqual(resp.status_code, 200)
        # Guest order creation should succeed and create a provisional Customer
        url = reverse("order-create")
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 201)
        order = Order.objects.get(id=resp.json()["id"])
        self.assertIsNotNone(order.customer)
        self.assertEqual(order.customer.user.username, self.client.session.get('_auth_user_id'))

    def test_order_creation_insufficient_stock(self):
        # Attempt to add more items than stock
        resp = self._add_to_cart(5, user=self.user)
        self.assertEqual(resp.status_code, 400)
        self.assertIn("Insufficient stock", resp.json().get("detail"))

    def test_order_creation_empty_cart(self):
        # No items in cart
        url = reverse("order-create")
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 400)
        self.assertIn("cart", resp.json().get("detail", ""))
