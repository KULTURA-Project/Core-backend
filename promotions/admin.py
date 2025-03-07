from django.contrib import admin
from .models import PromoType, Coupon, Promotion, ProductPromo

# Inline for managing ProductPromos within Promotion admin
class ProductPromoInline(admin.TabularInline):
    model = ProductPromo
    extra = 1  # Number of empty forms to display by default
    raw_id_fields = ('product_inventory',)  # Use raw ID fields for ForeignKeys


@admin.register(PromoType)
class PromoTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('name', 'coupon_code')
    search_fields = ('name', 'coupon_code')


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'promo_reduction', 'promo_start', 'time_end', 'is_active', 'promo_type')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'promo_type')  # Add filters for active status and type
    inlines = [ProductPromoInline]  # Inline editing for related ProductPromos


@admin.register(ProductPromo)
class ProductPromoAdmin(admin.ModelAdmin):
    list_display = ('product_inventory', 'promotion', 'price_override', 'promo_price')
    raw_id_fields = ('product_inventory', 'promotion')  # Use raw ID fields for ForeignKeys
