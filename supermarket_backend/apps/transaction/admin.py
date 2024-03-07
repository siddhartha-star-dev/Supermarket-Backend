from django.contrib import admin

from supermarket_backend.apps.transaction.models import Bill, BillItem


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ["total_amount", "created_at"]
    search_fields = ["total_amount"]
    list_filter = ["created_at"]
    date_hierarchy = "created_at"


@admin.register(BillItem)
class BillItemAdmin(admin.ModelAdmin):
    list_display = ["bill", "item", "quantity", "price"]
    search_fields = ["bill", "item"]
    list_filter = ["bill", "item"]
