from django.contrib import admin
from .models import Stock
from .forms import StockForm


class StockFormAdmin(admin.ModelAdmin):
   list_display = ['category', 'part_number', 'bin_location', 'name', 'quantity', 'reorder_level']
   form = StockForm
   list_filter = ['category']
   search_fields = ['category', 'name']

admin.site.register(Stock, StockFormAdmin)