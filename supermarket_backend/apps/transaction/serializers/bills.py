from rest_framework import serializers

from supermarket_backend.apps.inventory.serializers import ItemSerializer
from supermarket_backend.apps.transaction.models import Bill, BillItem
from supermarket_backend.apps.inventory.models import Item


class BillItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = BillItem
        fields = ["item", "quantity", "price"]


class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True)

    class Meta:
        model = Bill
        fields = ["items", "total_amount", "created_at"]
