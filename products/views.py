from rest_framework import viewsets
from .models import Product, Category, ProductType, ProductAttribute, ProductAttributeValue
from inventory.models import ProductInventory
from media.models import Media
from promotions.models import Promotion, ProductPromo
from .serializers import (ProductSerializer, CategorySerializer, ProductTypeSerializer,
                          ProductAttributeSerializer, ProductAttributeValueSerializer,
                          ProductInventorySerializer, MediaSerializer, PromotionSerializer,
                          ProductPromoSerializer)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer

class ProductAttributeValueViewSet(viewsets.ModelViewSet):
    queryset = ProductAttributeValue.objects.all()
    serializer_class = ProductAttributeValueSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductInventoryViewSet(viewsets.ModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class ProductPromoViewSet(viewsets.ModelViewSet):
    queryset = ProductPromo.objects.all()
    serializer_class = ProductPromoSerializer
