from rest_framework import generics, permissions
from core import models
from core.models import Product, Category, Brand
from . import serializers
from rest_framework.response import Response

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

# Cart endpoint
class CartView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CartSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cart, _ = models.Cart.objects.get_or_create(customer=request.user.customer_profile)
        else:
            session_id = request.session.session_key or request.session.create()
            cart, _ = models.Cart.objects.get_or_create(session_id=session_id)
        serializer = self.serializer_class(cart)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'detail': 'Product not found'}, status=404)
        if request.user.is_authenticated:
            cart, _ = models.Cart.objects.get_or_create(customer=request.user.customer_profile)
            customer = request.user.customer_profile
            session_id = None
        else:
            session_id = request.session.session_key or request.session.create()
            cart, _ = models.Cart.objects.get_or_create(session_id=session_id)
            customer = None
        cart_item, created = models.CartItem.objects.get_or_create(
            product=product,
            customer=customer,
            session_id=session_id,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        cart.items.add(cart_item)
        serializer = self.serializer_class(cart)
        return Response(serializer.data, status=200)
