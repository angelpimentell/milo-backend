from rest_framework.serializers import ModelSerializer

from models import User, Cart, Invoice


class UserSerializer(ModelSerializer):
    class Meta:
        model = User


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
