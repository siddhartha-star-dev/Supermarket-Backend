from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
)
from supermarket_backend.apps.inventory.serializers import ItemSerializer
from supermarket_backend.apps.inventory.models.items import Item


class ItemViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    http_method_names = ["get", "post", "patch", "delete"]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
