from rest_framework.serializers import ModelSerializer

from ..models import Cart


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "done", "created_at", "updated_at"]
