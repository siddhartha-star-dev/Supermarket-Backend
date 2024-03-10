from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
)
from rest_framework.decorators import action
from supermarket_backend.apps.transaction.models import Bill
from supermarket_backend.apps.transaction.serializers import BillSerializer


class BillViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    http_methods = ["get", "post", "patch", "delete"]
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bill.objects.all().order_by("-created_at")

    @action(methods=["GET"], detail=True)
    def print(self, request, *args, **kwargs):
        queryset = self.get_object()
        print(queryset)
        serializer = BillSerializer(instance=queryset)

        return Response(serializer.data)
