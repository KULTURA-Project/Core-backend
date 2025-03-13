# products/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Product
from inventory.models import ProductInventory
from media.models import Media
from promotions.models import ProductPromo , Promotion
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# products/forms.py
from django import forms
from .models import Product
from promotions.models import Promotion, ProductPromo
# products/forms.py

from inventory.models import ProductInventory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'product_type', 'is_active')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'product_type': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ProductInventoryForm(forms.ModelForm):
    class Meta:
        model = ProductInventory
        fields = ('product',)

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ('image', 'alt_text', 'is_feature')
        widgets = {
            'alt_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alt Text'}),
            'is_feature': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ('name', 'description', 'promo_reduction', 'coupon', 'promo_start', 'time_end', 'is_active', 'is_scheduled', 'promo_type')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Promotion Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'promo_reduction': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Promo Reduction'}),
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
        fields = ('product_inventory', 'promotion', 'price_override', 'promo_price')
        widgets = {
            'product_inventory': forms.Select(attrs={'class': 'form-select'}),
            'promotion': forms.Select(attrs={'class': 'form-select'}),
            'price_override': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price Override'}),
            'promo_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Promo Price'}),
        }
