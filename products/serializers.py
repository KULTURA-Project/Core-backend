from rest_framework import serializers
from .models import Product, Category, ProductType, ProductAttribute, ProductAttributeValue  , ProductTypeAttribute
from inventory.models import ProductInventory
from media.models import Media
from promotions.models import Promotion, ProductPromo
class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent', 'is_active', 'children']

    def get_children(self, obj):
        """Get all the child categories for the root category"""
        serializer = CategorySerializer(obj.children.all(), many=True)
        return serializer.data


class ProductTypeAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypeAttribute
        fields = ['id', 'product_attribute']

class ProductTypeSerializer(serializers.ModelSerializer):
    product_type_attributes = serializers.SerializerMethodField()

    class Meta:
        model = ProductType
        fields = ['id', 'name', 'product_type_attributes']

    def get_product_type_attributes(self, obj):
        # Assuming you want the IDs of the associated ProductAttributes
        return [attribute.product_attribute.id for attribute in obj.producttypeattribute_set.all()]

class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        fields = ['id', 'product_attribute', 'attribute_value']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'web_id', 'slug', 'name', 'description', 'category', 'product_type', 'is_active', 'created_at', 'updated_at']

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ['id', 'sku', 'upc', 'product_type', 'product', 'brand', 'is_active', 'is_default', 'retail_price', 'store_price', 'is_digital',
                 'weight', 'created_at', 'updated_at']

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'product_inventory', 'img_url', 'alt_text', 'is_feature', 'created_at', 'updated_at']

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'coupon', 'promo_start', 'time_end', 'is_active', 'is_scheduled', 'promo_type']

class ProductPromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPromo
        fields = ['id', 'product_inventory_id', 'promotion_id', 'price_override', 'promo_price']