from django.db import models


class ProductCart(models.Model):
    product = models.ForeignKey("stock.Product", on_delete=models.CASCADE)
    cart = models.ForeignKey("sales.Cart", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products_carts"
