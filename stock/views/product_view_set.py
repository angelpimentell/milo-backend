from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from ..models import Product
from ..serializers import ProductSerializer


class ProductViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView,
                     viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
