from rest_framework import serializers

from supermarket_backend.apps.inventory.models.items import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Item
