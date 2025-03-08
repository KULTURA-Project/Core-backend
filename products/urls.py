from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'producttypes', views.ProductTypeViewSet)
router.register(r'productattributes', views.ProductAttributeViewSet)
router.register(r'productattributevalues', views.ProductAttributeValueViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'productinventories', views.ProductInventoryViewSet)
router.register(r'media', views.MediaViewSet)
router.register(r'promotions', views.PromotionViewSet)
router.register(r'productpromos', views.ProductPromoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
