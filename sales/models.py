from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "users"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField()

    class Meta:
        db_table = "carts"


class Invoice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    paid = models.BooleanField()

    class Meta:
        db_table = "orders"
