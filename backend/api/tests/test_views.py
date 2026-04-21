"""Minimal functional tests for the API views.

These tests use Django's ``Client`` to hit the list and cart endpoints.
They avoid complex authentication by using the default test user.
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from core import models
from core.models import Product, Category, Brand
from django.urls import reverse

User = get_user_model()


class ApiViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create sample data
        self.brand = Brand.objects.create(name="TestBrand")
        self.category = Category.objects.create(name="TestCat")
        self.product = Product.objects.create(
            name="TestProd", brand=self.brand, category=self.category, price=10.0, stock=5
        )
        self.user = User.objects.create_user(username="user", password="pw")

    def test_brand_list(self):
        url = reverse("brand-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("TestBrand", resp.content.decode())

    def test_product_list(self):
        url = reverse("product-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("TestProd", resp.content.decode())

    def test_cart_add_unauthenticated(self):
        url = reverse("cart")
        payload = {"product_id": self.product.id, "quantity": 2}
        resp = self.client.post(url, payload)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertIn("items", data)
        self.assertEqual(len(data["items"]), 1)
        self.assertEqual(data["items"][0]["quantity"], 2)

    def test_cart_add_authenticated(self):
        self.client.login(username="user", password="pw")
        url = reverse("cart")
        payload = {"product_id": self.product.id, "quantity": 1}
        resp = self.client.post(url, payload)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertIn("items", data)
        self.assertEqual(len(data["items"]), 1)
        self.assertEqual(data["items"][0]["quantity"], 1)
