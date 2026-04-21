"""Unit tests for the API serializers.

The tests cover both read‑only nested serializers and writable fields
such as the ``PaymentSerializer`` which expects an order id.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models
from api import serializers

User = get_user_model()


class SerializerTestCase(TestCase):
    def setUp(self):
        # Common objects used across tests
        self.brand = models.Brand.objects.create(name="BrandX")
        self.category = models.Category.objects.create(name="CatY")
        self.product = models.Product.objects.create(
            name="ProductZ", brand=self.brand, category=self.category, price=99.99, stock=20
        )
        self.user = User.objects.create_user(username="tester", password="pw")
        self.customer = models.Customer.objects.create(user=self.user)
        self.cart = models.Cart.objects.create(customer=self.customer)
        self.cart_item = models.CartItem.objects.create(
            product=self.product, quantity=2, customer=self.customer
        )
        self.cart.items.add(self.cart_item)
        self.order = models.Order.objects.create(customer=self.customer)
        self.order_item = models.OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
            price_at_purchase=self.product.price,
        )
        self.order.items.add(self.order_item)

    def test_brand_serializer(self):
        data = serializers.BrandSerializer(self.brand).data
        self.assertEqual(set(data.keys()), {"id", "name"})
        self.assertEqual(data["name"], "BrandX")

    def test_category_serializer(self):
        data = serializers.CategorySerializer(self.category).data
        self.assertEqual(set(data.keys()), {"id", "name"})
        self.assertEqual(data["name"], "CatY")

    def test_product_serializer_nested(self):
        data = serializers.ProductSerializer(self.product).data
        self.assertIn("brand", data)
        self.assertIn("category", data)
        self.assertEqual(data["brand"]["name"], "BrandX")
        self.assertEqual(data["category"]["name"], "CatY")
        self.assertEqual(data["price"], 99.99)

    def test_cart_serializer(self):
        data = serializers.CartSerializer(self.cart).data
        self.assertIn("items", data)
        self.assertEqual(len(data["items"]), 1)
        self.assertEqual(data["items"][0]["quantity"], 2)
        self.assertEqual(data["items"][0]["product"]["name"], "ProductZ")

    def test_order_serializer(self):
        data = serializers.OrderSerializer(self.order).data
        # ``customer`` is represented as a string (username)
        self.assertEqual(data["customer"], "tester")
        self.assertIn("items", data)
        self.assertEqual(len(data["items"]), 1)
        self.assertEqual(data["items"][0]["quantity"], 1)
        self.assertEqual(data["items"][0]["product"]["name"], "ProductZ")

    def test_payment_serializer_write(self):
        payload = {
            "order": self.order.id,
            "provider": "Stripe",
            "provider_id": "pay_001",
            "amount": 50.00,
            "status": "paid",
        }
        serializer = serializers.PaymentSerializer(data=payload)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        payment = serializer.save()
        self.assertEqual(payment.order, self.order)
        self.assertEqual(payment.provider_id, "pay_001")
        self.assertEqual(payment.amount, 50.00)
