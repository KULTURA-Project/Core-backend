from django.contrib import admin
from .models import Media

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('product_inventory', 'img_url', 'alt_text', 'is_feature')
    search_fields = ('alt_text', 'img_url')
    list_filter = ('is_feature',)
    raw_id_fields = ('product_inventory',)