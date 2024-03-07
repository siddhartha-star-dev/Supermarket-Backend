from django.db import models

from supermarket_backend.apps.inventory.models import Item


class Bill(models.Model):
    items = models.ManyToManyField(Item, through="BillItem")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill #{self.pk}"


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} {self.item.name} in Bill #{self.bill.pk}"
