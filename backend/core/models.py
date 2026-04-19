"""Core data models for the e‑commerce backend.

The repository currently contains only placeholder files.  The
``core`` app is the place where we will model the business entities
required for the MVP: categories, brands, products, variants, stock,
customers, orders, order items, payments and shipping addresses.

We keep the models lean and database‑centric – Django’s ORM will
generate the migrations.  Validation logic is intentionally minimal
so that the API layer can handle most of the business rules.
"""

from __future__ import annotations

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

__all__ = [
    "Category",
    "Brand",
    "Product",
    "Variant",
    "Inventory",
    "Customer",
    "Order",
    "OrderItem",
    "Payment",
    "ShippingAddress",
]


class Category(models.Model):
    """Product grouping for navigation and filtering."""

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class Brand(models.Model):
    """Manufacturer or label for a product."""

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class Product(models.Model):
    """A product can have multiple variants (size, color, etc.)."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="products")
    categories = models.ManyToManyField(Category, related_name="products", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class Variant(models.Model):
    """Specific SKU of a product (size/color/etc.)."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    sku = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    attributes = models.JSONField(blank=True, default=dict)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["product", "sku"]
        verbose_name = "Variant"
        verbose_name_plural = "Variants"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.product.name} - {self.sku}"


class Inventory(models.Model):
    """Tracks stock for each variant."""

    variant = models.OneToOneField(Variant, on_delete=models.CASCADE, related_name="inventory")
    quantity = models.PositiveIntegerField(default=0)
    reserved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.variant} qty={self.quantity}"


class Customer(models.Model):
    """Extended user profile for customers."""

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="customer_profile")
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.user.get_full_name() or self.user.username


class Order(models.Model):
    """A customer's order. Only essential fields for MVP."""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(
        max_length=32,
        choices=[("created", "Created"), ("paid", "Paid"), ("shipped", "Shipped"), ("canceled", "Canceled")],
        default="created",
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipping_address = models.ForeignKey(
        "ShippingAddress",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"Order #{self.id} ({self.status})"


class OrderItem(models.Model):
    """Line item in an order."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.quantity}x {self.variant}"


class Payment(models.Model):
    """Payment record for an order – very simple for MVP."""

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    provider = models.CharField(max_length=64)
    reference = models.CharField(max_length=128, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=32,
        choices=[("pending", "Pending"), ("completed", "Completed"), ("failed", "Failed")],
        default="pending",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.provider} #{self.reference} ({self.status})"


class ShippingAddress(models.Model):
    """Shipping address for an order – minimal fields for MVP."""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.street}, {self.city}"
