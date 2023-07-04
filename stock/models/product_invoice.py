from django.db import models

from constants import DECIMAL_PLACES, MAX_DIGITS


class ProductInvoice(models.Model):
    product = models.ForeignKey("stock.Product", on_delete=models.CASCADE)
    cart = models.ForeignKey("sales.Invoice", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=MAX_DIGITS + DECIMAL_PLACES, decimal_places=DECIMAL_PLACES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products_invoices"
