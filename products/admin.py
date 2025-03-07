from django.contrib import admin
from inventory.models import ProductInventory, ProductAttributeValues
from media.models import Media
from promotions.models import ProductPromo
from .models import Product, Category, ProductType, ProductAttribute, ProductAttributeValue, ProductTypeAttribute

# Inline for managing Media directly within the ProductInventory admin
class MediaInline(admin.TabularInline):
    model = Media
    extra = 1
    fields = ('img_url', 'alt_text', 'is_feature')
    readonly_fields = ('created_at', 'updated_at')

# Inline for managing Attribute Values directly within the ProductInventory admin
class ProductAttributeValuesInline(admin.TabularInline):
    model = ProductAttributeValues
    extra = 1
    raw_id_fields = ('attribute_value',)

# Inline for managing Promotions directly within the ProductInventory admin
class ProductPromoInline(admin.TabularInline):
    model = ProductPromo
    extra = 1
    raw_id_fields = ('promotion',)

# Inline for ProductInventory
class ProductInventoryInline(admin.TabularInline):
    model = ProductInventory
    extra = 1
    raw_id_fields = ('product_type',)
    inlines = [
        MediaInline,
        ProductAttributeValuesInline,
        ProductPromoInline,
    ]
    fields = (
        'sku',
        'product_type',
        'is_active',
        'is_default',
        'retail_price',
        'store_price',
        'is_digital',
        'weight',
    )

# Inline for Category
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
    fields = ('name', 'slug', 'parent', 'is_active')
    prepopulated_fields = {'slug': ('name',)}

# Inline for ProductType
class ProductTypeInline(admin.TabularInline):
    model = ProductType
    extra = 0
    fields = ('name',)

# Inline for ProductAttribute
class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 0
    fields = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'web_id', 'category', 'product_type', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'web_id', 'description', 'category__name', 'product_type__name')
    list_filter = ('category', 'product_type', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)

    inlines = [
        ProductInventoryInline
        ]
    
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductTypeAttribute)
#admin.site.register(Product, ProductAdmin)
