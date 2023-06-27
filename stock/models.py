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


class ProductCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey("sales.Cart", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products_carts"


class ProductInvoice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey("sales.Invoice", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=MAX_DIGITS + DECIMAL_PLACES, decimal_places=DECIMAL_PLACES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products_invoices"
