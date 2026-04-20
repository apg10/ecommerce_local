from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('brands/', views.BrandList.as_view(), name='brand-list'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('payments/create/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('cart/', views.CartView.as_view(), name='cart'),
    # Auth endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
