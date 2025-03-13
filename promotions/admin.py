from django.contrib import admin
from .models import PromoType, Coupon, Promotion, ProductPromo
from unfold.admin import ModelAdmin

# Inline for managing ProductPromos within Promotion admin
class ProductPromotionInline(admin.TabularInline):
    model = ProductPromo
    extra = 1
    autocomplete_fields = ['product_inventory']  # Corrected field
    fields = ('product_inventory', 'promotion', 'price_override', 'promo_price')
class PromotionInline(admin.TabularInline):
    model = ProductPromo
    extra = 1
    autocomplete_fields = ['promotion']
    fields = ('promotion', 'price_override', 'promo_price', 'active_dates')
# Admin registrations
@admin.register(PromoType)
class PromoTypeAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Coupon)
class CouponAdmin(ModelAdmin):
    list_display = ('name', 'coupon_code')
    search_fields = ('name', 'coupon_code')

@admin.register(Promotion)
class PromotionAdmin(ModelAdmin):
    list_display = ('name', 'promo_reduction', 'promo_start', 'time_end', 'is_active', 'promo_type')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'promo_type')  # Add filters for active status and type
    inlines = []  # Inline editing for related ProductPromos

class ProductPromoInline(admin.TabularInline):
    model = ProductPromo
    extra = 1
    autocomplete_fields = ['product_inventory']  # This should be removed since it's the parent model