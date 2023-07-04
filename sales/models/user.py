from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from ..managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    is_superuser = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "users"
