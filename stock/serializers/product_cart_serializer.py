from rest_framework.serializers import ModelSerializer

from ..models import ProductCart


class ProductCartSerializer(ModelSerializer):
    class Meta:
        model = ProductCart
        fields = ["id", "product", "cart", "created_at", "updated_at"]
