# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.BrandList.as_view(), name='brand-list'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('products/', views.ProductList.as_view(), name='product-list'),
]
