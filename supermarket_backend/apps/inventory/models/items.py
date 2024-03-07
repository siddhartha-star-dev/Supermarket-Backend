from django.db import models


class Item(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "items"
        verbose_name = "Item"
        verbose_name_plural = "Items"
