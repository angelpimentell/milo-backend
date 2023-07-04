from django.db import models

from constants import DECIMAL_PLACES, MAX_DIGITS


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=MAX_DIGITS + DECIMAL_PLACES, decimal_places=DECIMAL_PLACES)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"
