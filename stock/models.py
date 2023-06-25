from django.db import models

from constants import DECIMAL_PLACES, MAX_DIGITS

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)

    class Meta:
        db_table = "products"


class ProductCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey("sales.Cart", on_delete=models.CASCADE)

    class Meta:
        db_table = "products_carts"


class ProductInvoice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey("sales.Invoice", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)

    class Meta:
        db_table = "products_invoices"
