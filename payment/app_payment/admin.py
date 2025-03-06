from django.contrib import admin
from .models import Item#, Order

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency')
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'created_at', 'total_price')
#     filter_horizontal = ('items',)

