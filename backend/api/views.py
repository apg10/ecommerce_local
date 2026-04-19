from rest_framework import generics, permissions
from core import models
from core.models import Product, Category, Brand
from . import serializers

class BrandList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Brand.objects.filter(is_active=True)
    serializer_class = serializers.BrandSerializer

class CategoryList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.filter(is_active=True)
    serializer_class = serializers.CategorySerializer

class ProductList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.filter(is_active=True)
    serializer_class = serializers.ProductSerializer

class OrderList(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderCreateView(generics.CreateAPIView):
    serializer_class = serializers.OrderSerializer
    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        if user:
            customer = getattr(user, 'customer_profile', None)
            if not customer:
                customer = models.Customer.objects.create(user=user)
            serializer.save(customer=customer)
        else:
            serializer.save(customer=None)

class PaymentCreateView(generics.CreateAPIView):
    serializer_class = serializers.PaymentSerializer

