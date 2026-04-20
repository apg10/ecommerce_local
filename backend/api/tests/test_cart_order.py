from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from core.models import Product, Category, Brand
from django.urls import reverse


class CartOrderTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="tester", password="pass")
        self.brand = Brand.objects.create(name="B1")
        self.category = Category.objects.create(name="C1")
        self.product = Product.objects.create(
            name="Prod1",
            brand=self.brand,
            category=self.category,
            price=10.00,
            stock=5,
        )
        self.cart_url = reverse("cart")

    def test_add_to_cart_authenticated(self):
        self.client.login(username="tester", password="pass")
        response = self.client.post(self.cart_url, {"product_id": self.product.id, "quantity": 2})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("items", data)
        self.assertEqual(len(data["items"]), 1)
        self.assertEqual(data["items"][0]["quantity"], 2)

    def test_add_to_cart_insufficient_stock(self):
        self.client.login(username="tester", password="pass")
        response = self.client.post(self.cart_url, {"product_id": self.product.id, "quantity": 10})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Insufficient stock", response.json().get("detail", ""))
