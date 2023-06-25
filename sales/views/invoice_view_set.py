from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from ..models import Invoice
from ..serializers import InvoiceSerializer


class InvoiceViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView,
                     viewsets.ViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
