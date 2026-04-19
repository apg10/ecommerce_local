from django.contrib import admin
from .models import Brand, Category, Product, Variant, Inventory, Customer, Order, OrderItem, Payment, ShippingAddress

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    search_fields = ("name", "slug")
    list_filter = ("is_active",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    search_fields = ("name", "slug")
    list_filter = ("is_active",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "brand", "is_active")
    search_fields = ("name", "slug", "brand__name")
    list_filter = ("is_active", "brand")
    filter_horizontal = ("categories",)

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ("sku", "product", "price", "is_active")
    search_fields = ("sku", "product__name")
    list_filter = ("is_active", "product")

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("variant", "quantity", "reserved")
    search_fields = ("variant__sku",)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "phone")
    search_fields = ("user__username", "user__email")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "total", "created_at")
    search_fields = ("id", "customer__user__username")
    list_filter = ("status", "created_at")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "variant", "quantity", "unit_price")
    search_fields = ("order__id", "variant__sku")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "provider", "reference", "amount", "status", "created_at")
    search_fields = ("reference", "provider")

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("customer", "street", "city", "country")
    search_fields = ("customer__user__username", "street", "city")

