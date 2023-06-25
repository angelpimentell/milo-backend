from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from ..models import User
from ..serializers import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView,
                  viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
