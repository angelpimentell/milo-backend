from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Invoice
from ..serializers import InvoiceSerializer
from ..permissions import AuthenticatedReadOnlyPermission


class InvoiceViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView,
                     viewsets.ViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated & AuthenticatedReadOnlyPermission]

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)
