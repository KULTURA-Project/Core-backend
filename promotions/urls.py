# promotions/urls.py
from django.urls import path
from . import views

app_name = 'promotions'

urlpatterns = [
    path('', views.promotion_list, name='promotion_list'),
    path('add/', views.add_promotion, name='add_promotion'),
    path('edit/<pk>/', views.edit_promotion, name='edit_promotion'),
    path('delete/<pk>/', views.delete_promotion, name='delete_promotion'),
    
    path('coupons/', views.coupon_list, name='coupon_list'),
    path('coupons/add/', views.add_coupon, name='add_coupon'),
    path('coupons/edit/<pk>/', views.edit_coupon, name='edit_coupon'),
    path('coupons/delete/<pk>/', views.delete_coupon, name='delete_coupon'),
]
