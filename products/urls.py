# products/urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [

    path('add/', views.add_product, name='add_product'),
    
    path('products/', views.product_list, name='product_list'),
  # products/urls.py
path('edit/<pk>/', views.edit_product, name='edit_product'),

  path('delete/<pk>/', views.delete_product, name='delete_product'),
  
     path('admin/get_subcategories/', views.get_subcategories, name='get_subcategories'),
]
