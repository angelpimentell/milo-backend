from rest_framework.serializers import ModelSerializer

from .models import Product, ProductCart, ProductInvoice


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "quantity", "price", "created_at", "updated_at"]


class ProductCartSerializer(ModelSerializer):
    class Meta:
        model = ProductCart
        fields = ["id", "product", "cart", "created_at", "updated_at"]


class ProductInvoiceSerializer(ModelSerializer):
    class Meta:
        model = ProductInvoice
        fields = ["id", "product", "cart", "price", "created_at", "updated_at"]
