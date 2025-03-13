# media/admin.py
from django.contrib import admin
from .models import Media
from unfold.admin import ModelAdmin
class MediaAdmin(ModelAdmin):
    list_display = ('product', 'image', 'is_feature', 'created_at')
    list_filter = ('is_feature', 'created_at')
    search_fields = ('product__name',)

admin.site.register(Media, MediaAdmin)