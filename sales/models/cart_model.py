from django.db import models


class Cart(models.Model):
    user = models.ForeignKey("sales.User", on_delete=models.CASCADE)
    done = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "carts"
