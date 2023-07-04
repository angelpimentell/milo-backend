from rest_framework.serializers import ModelSerializer

from ..models import Invoice


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = ["id", "user", "name", "paid", "created_at", "updated_at"]
