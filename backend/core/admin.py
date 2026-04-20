from django.contrib import admin
from . import models

@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category", "price", "stock", "is_active")
    search_fields = ("name", "brand__name", "category__name")
    list_filter = ("brand", "category", "is_active")

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phone", "address")
    search_fields = ("user__username", "phone")

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "session_id", "created_at")
    search_fields = ("customer__user__username", "session_id")

@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "customer", "session_id")
    search_fields = ("product__name", "customer__user__username")

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "total", "created_at", "updated_at")
    search_fields = ("customer__user__username", "status")
    list_filter = ("status", "created_at")

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "price_at_purchase")
    search_fields = ("order__id", "product__name")

@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "provider", "provider_id", "amount", "status", "created_at")
    search_fields = ("order__id", "provider", "provider_id")
    list_filter = ("status", "created_at")
