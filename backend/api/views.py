# views.py
from rest_framework import generics
from core.models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer

class BrandList(generics.ListAPIView):
    queryset = Brand.objects.filter(is_active=True)
    serializer_class = BrandSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

