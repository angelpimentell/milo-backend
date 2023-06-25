from rest_framework.serializers import ModelSerializer

from .models import User, Cart, Invoice


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "created_at", "updated_at"]


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "done", "created_at", "updated_at"]


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = ["id", "user", "name", "paid", "created_at", "updated_at"]
