# products/urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [

    path('products/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
  # products/urls.py
path('edit/<pk>/', views.edit_product, name='edit_product'),

  path('delete/<pk>/', views.delete_product, name='delete_product'),
]
