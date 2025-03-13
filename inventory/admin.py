# inventory/admin.py
from django.contrib import admin
from .models import ProductInventory 
from products.admin import ProductAttributeValuesInline
from unfold.admin import ModelAdmin
@admin.register(ProductInventory)
class ProductInventoryAdmin(ModelAdmin):
    list_display = ('sku', 'product', 'store_price', 'stock_status')
    #list_filter = ('is_active', 'product__product_type') 
    search_fields = ('sku', 'upc', 'product__name')
    inlines = [ProductAttributeValuesInline ]
    
    def stock_status(self, obj):
        return format_html(
            '<div class="stock-indicator {}"></div>', 
            "in-stock" if obj.is_active else "out-of-stock"
        )
    stock_status.short_description = "Stock Status"
