from rest_framework.serializers import ModelSerializer

from models import Product, ProductCart, ProductInvoice


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product


class ProductCartSerializer(ModelSerializer):
    class Meta:
        model = ProductCart


class ProductInvoiceSerializer(ModelSerializer):
    class Meta:
        model = ProductInvoice
