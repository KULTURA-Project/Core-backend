from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, ProductAttribute, ProductAttributeValue, Category , ProductTypeAttribute
from inventory.models import ProductInventory
from media.models import Media
from promotions.models import ProductPromo, Promotion


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'product_type', 'is_active']




class ProductInventoryForm(forms.ModelForm):
    class Meta:
        model = ProductInventory
        fields = ['sku', 'upc', 'product_type', 'product', 'retail_price', 'store_price', 'is_digital', 'weight', 'is_active', 'is_default']
        widgets = {
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU'}),
            'upc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UPC'}),
            'product_type': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'retail_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Retail Price'}),
            'store_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Store Price'}),
            'is_digital': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_default': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['image', 'alt_text', 'is_feature']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'alt_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alt Text'}),
            'is_feature': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

'''
class ProductAttributeValueForm(forms.ModelForm):
    class Meta:
        model = ProductAttributeValue
        fields = ['attribute_value']
        widgets = {
            'attribute_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Attribute Value'}),
        }'''


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['name', 'description', 'promo_reduction', 'coupon', 'promo_start', 'time_end', 'is_active', 'is_scheduled', 'promo_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Promotion Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Promotion Description'}),
            'promo_reduction': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Promo Reduction %'}),
            'coupon': forms.Select(attrs={'class': 'form-select'}),
            'promo_start': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'time_end': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_scheduled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'promo_type': forms.Select(attrs={'class': 'form-select'}),
        }


class ProductPromoForm(forms.ModelForm):
    class Meta:
        model = ProductPromo
        fields = ['product_inventory', 'promotion', 'price_override', 'promo_price']
        widgets = {
            'product_inventory': forms.Select(attrs={'class': 'form-select'}),
            'promotion': forms.Select(attrs={'class': 'form-select'}),
            'price_override': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price Override'}),
            'promo_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Promo Price'}),
        }


class ProductAttributeForm(forms.ModelForm):
    class Meta:
        model = ProductAttribute
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Attribute Name'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'parent': forms.Select(attrs={'class': 'form-select'}),
        }
