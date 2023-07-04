from rest_framework.serializers import ModelSerializer

from ..models import ProductInvoice


class ProductInvoiceSerializer(ModelSerializer):
    class Meta:
        model = ProductInvoice
        fields = ["id", "product", "cart", "price", "created_at", "updated_at"]
