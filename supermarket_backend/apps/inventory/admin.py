from django.contrib import admin

from supermarket_backend.apps.inventory.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "company"]
