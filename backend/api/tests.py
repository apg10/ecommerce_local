from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from core.models import Product, Category, Brand, Customer
from django.urls import reverse

class CartViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="testuser", password="pass")
        self.brand = Brand.objects.create(name="TestBrand")
        self.category = Category.objects.create(name="TestCat")
        self.product = Product.objects.create(
            name="TestProduct",
            brand=self.brand,
            category=self.category,
            price=10.00,
            is_active=True,
            stock=5  # add stock field for tests
        )
        self.cart_url = reverse('cart')
        self.add_url = self.cart_url

    def test_add_with_sufficient_stock(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.post(self.add_url, {"product_id": self.product.id, "quantity": 3})
        self.assertEqual(response.status_code, 200)

    def test_add_exceeding_stock(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.post(self.add_url, {"product_id": self.product.id, "quantity": 10})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Insufficient stock", response.json()["detail"]) 
