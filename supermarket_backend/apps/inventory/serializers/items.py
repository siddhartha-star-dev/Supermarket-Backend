from rest_framework import serializers

from supermarket_backend.apps.inventory.models.items import Item


class ItemSerializer(serializers.Serializer):
    class Meta:
        fields = "__all__"
        model = Item
