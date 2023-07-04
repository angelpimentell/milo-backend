from django.db import models


class Invoice(models.Model):
    user = models.OneToOneField("sales.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    paid = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "invoices"
