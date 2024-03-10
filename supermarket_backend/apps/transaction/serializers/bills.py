from rest_framework import serializers

from supermarket_backend.apps.inventory.serializers import ItemSerializer
from supermarket_backend.apps.transaction.models import Bill, BillItem


class BillItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = BillItem
        fields = ["item", "quantity", "price"]


class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ("total_amount", "created_at", "items")
