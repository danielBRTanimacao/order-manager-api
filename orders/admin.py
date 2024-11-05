from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'client',
        'product',
        'amount',
        'total_price',
        'status'
    ]
    ordering = ['-id']
    search_fields = ['id', 'client', 'product']
    list_editable = ['amount', 'total_price']
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = ['id', 'client', 'product']