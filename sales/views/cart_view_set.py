from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from ..models import Cart
from ..serializers import CartSerializer


class CartViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView,
                  viewsets.ViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
