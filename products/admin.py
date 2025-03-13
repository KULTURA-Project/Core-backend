# products/admin.py
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from django.db.models import Prefetch
from .models import (
    Product, Category, ProductType,
    ProductAttribute, ProductAttributeValue,
    ProductInventory, ProductTypeAttribute,
)
from inventory.models import ProductAttributeValues
from media.models import Media
from promotions.models import Promotion, ProductPromo
from django.db.models import F, Count, Sum
from promotions.admin import PromotionInline, ProductPromoInline
from django.utils.translation import gettext_lazy as _
from django import forms

# ======================
# INLINE ADMIN CLASSES
# ======================

class ProductAttributeValuesInline(TabularInline):
    model = ProductAttributeValues  # Directly use the through model
    extra = 1
    verbose_name = "Attribute Value"
    verbose_name_plural = "Product Attributes"

    def get_formset(self, request, obj=None, **kwargs):
        # Get the product inventory instance
        if obj:
            product_type = obj.product_type
            self.attribute_queryset = ProductAttributeValue.objects.filter(
                product_attribute__product_type=product_type
            )
        else:
            self.attribute_queryset = ProductAttributeValue.objects.none()

        return super().get_formset(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "attribute_value":
            kwargs["queryset"] = self.attribute_queryset
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class ProductInventoryForm(forms.ModelForm):
    class Meta:
        model = ProductInventory
        fields = ['sku', 'upc', 'is_active', 'is_default',
                  'retail_price', 'store_price', 'weight', 'product_type', 'product']  # Include product_type and product
        widgets = {
            'product_type': forms.Select(attrs={'class': 'form-control'}),  # Optional styling
            'product': forms.Select(attrs={'class': 'form-control'}),  # Optional styling
        }
        help_texts = {
            'product_type': _('Select the type of product.')
        }
        labels = {
            'retail_price': _('Retail Price'),
            'store_price': _('Store Price'),
            'weight': _('Item Weight'),
            'sku': _('SKU'),
            'upc': _('UPC'),
        }
class ProductInventoryInline(StackedInline):
    model = ProductInventory
    extra = 1
    form = ProductInventoryForm  # Applying the custom form here
    inlines = [ProductAttributeValuesInline, ProductPromoInline]  # Nest both inlines here
    # REMOVE CLASSES=['COLLAPSE'] to make directly visible

    fields = (
        'sku', 'upc', 'is_active', 'is_default',
        'retail_price', 'store_price', 'weight', 'product_type', 'product'  # added product_type
    )
    verbose_name_plural = "Product Inventories" # Corrects plural

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sku')  # Order by SKU

class MediaInlineForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['image', 'alt_text', 'is_feature', 'product_inventory']
        widgets = {
           'image': forms.FileInput(attrs={'class': 'form-control'}),  # Add CSS class for styling
           'alt_text': forms.TextInput(attrs={'class': 'form-control'}),  # Add CSS class for styling
            'is_feature': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Add CSS class for styling
           'product_inventory': forms.Select(attrs={'class': 'form-control'}),  # Add CSS class for styling
        }
        labels = {
            'image': _('Product Image'), # Renames image to "product image"
            'alt_text': _('Image Description'),
            'is_feature': _('Featured Image'),
            'product_inventory': _('Product Inventory'),
        }

class MediaInline(TabularInline):
    model = Media
    form = MediaInlineForm  # use form here
    extra = 1
    readonly_fields = ['image_preview'] # Add product inventory if needed
    fields = ('image', 'image_preview', 'alt_text', 'is_feature', 'product_inventory') # Now it's showing

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product_inventory':
            # Filter the queryset based on the current product
            if request.resolver_match.kwargs.get('object_id'):
                product = Product.objects.get(pk=request.resolver_match.kwargs['object_id'])
                kwargs['queryset'] = ProductInventory.objects.filter(product=product)
            else:
                kwargs['queryset'] = ProductInventory.objects.none()  # Empty queryset if no product
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    def image_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-height: 100px;"/>',
            obj.image.url
        ) if obj.image else ""
    image_preview.short_description = "Preview"

# ======================
# PRODUCT ADMIN CUSTOMIZATION
# ======================

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        'name', 'category', 'product_type',
        'status_badge', 'inventory_summary',
        'media_preview', 'current_promotions'
    )
    list_filter = ('category', 'product_type', 'is_active')
    search_fields = ('name', 'web_id', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [MediaInline]
    #ProductInventoryInline
    actions = ['activate_products', 'deactivate_products']

    # Custom fieldsets with tabs
    fieldsets = (
        ('Core Information', {
            'fields': (
                'web_id', 'name', 'slug',
                'description', 'category', 'product_type'
            )
        }),
        ('Status & Dates', {
            'fields': ('is_active', ('created_at', 'updated_at')),
            'classes': ('collapse',)
        }),
    )

    # ======================
    # CUSTOM METHODS
    # ======================

    @admin.display(description="Status")
    def status_badge(self, obj):
        color = "green" if obj.is_active else "red"
        return format_html(
            '<span style="color: {};">●</span> {}',
            color,
            "Active" if obj.is_active else "Inactive"
        )

    @admin.display(description="Inventory")
    def inventory_summary(self, obj):
        inventories = obj.product_inventory.all()
        count = inventories.count()
        prices = [inv.store_price for inv in inventories]
        low = min(prices) if prices else 0
        return format_html(
            "{} variants<br>From ${}",
            count, low
        )

    @admin.display(description="Media")
    def media_preview(self, obj):
        media = obj.media_set.all()[:3]
        previews = []
        for m in media:
            previews.append(
                f'<img src="{m.image.url}" style="max-height: 50px; margin-right: 5px;">'
            )
        return format_html(" ".join(previews)) if previews else "No images"

    @admin.display(description="Promotions")
    def current_promotions(self, obj):
        now = timezone.now()
        promotions = Promotion.objects.filter(
            productpromo__product_inventory__product=obj,
            promo_start__lte=now,
            time_end__gte=now
        ).distinct()
        return format_html(
            "<br>".join([f'<b>{p.name}</b> ({p.promo_reduction}%)' for p in promotions])
        )

    # ======================
    # CUSTOM ACTIONS
    # ======================

    @admin.action(description="Activate selected products")
    def activate_products(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Deactivate selected products")
    def deactivate_products(self, request, queryset):
        queryset.update(is_active=False)

    # ======================
    # OVERRIDES
    # ======================

    def get_readonly_fields(self, request, obj=None):
        readonly = ['created_at', 'updated_at']
        if obj:  # When editing an existing object
            readonly.append('web_id')
        return readonly

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(
            'media_set',
            'product_type',
            'product_inventory',
            'productpromo_set__promotion'
        )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        product = self.get_object(request, object_id)

        # Add dynamic attributes panel
        if product.product_type:
            attributes = product.product_type.attributes.all()
            extra_context['attributes'] = attributes

        # Add inventory summary
        inventory_data = product.product_inventory.annotate(
            variant_count=Count('id')
        ).aggregate(
            total_variants=Sum('variant_count'),
            min_price=Min('store_price')
        )
        extra_context['inventory_summary'] = inventory_data

        return super().change_view(
            request, object_id, form_url, extra_context=extra_context
        )

    def get_form(self, request, obj=None, **kwargs):
        # You can override the form here, but for dynamic fields, you'll need custom JS
        return super().get_form(request, obj, **kwargs)

# products/admin.py
from django.contrib import admin
from .models import Category

class CategoryInline(TabularInline):
    model = Category
    extra = 1
    fk_name = 'parent'  # Use 'parent' to show subcategories

class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'parent', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    inlines = [CategoryInline]  # Show subcategories inline

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('children')

@admin.register(ProductAttribute)
class ProductAttributeAdmin(ModelAdmin):
    list_display = ('name', 'product_type')
    search_fields = ('name',)

@admin.register(ProductType)
class ProductTypeAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# admin.py@admin.register(ProductAttributeValue)
@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(ModelAdmin):
    list_display = ('value', 'product_attribute')  # Use the correct field name
    search_fields = ('value',)

admin.site.register(Category, CategoryAdmin)
