# promotions/forms.py
from django import forms
from .models import Promotion, Coupon, PromoType

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ('name', 'description', 'promo_reduction', 'coupon', 'promo_start', 'time_end', 'is_active', 'is_scheduled', 'promo_type')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coupon'].queryset = Coupon.objects.all()
        self.fields['promo_type'].queryset = PromoType.objects.all()
        
        # Add custom styles to form fields
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Promotion Name'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 5})
        self.fields['promo_reduction'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Promo Reduction'})
        self.fields['coupon'].widget.attrs.update({'class': 'form-select'})
        self.fields['promo_start'].widget.attrs.update({'class': 'form-control', 'type': 'datetime-local'})
        self.fields['time_end'].widget.attrs.update({'class': 'form-control', 'type': 'datetime-local'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['is_scheduled'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['promo_type'].widget.attrs.update({'class': 'form-select'})

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ('name', 'coupon_code')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Coupon Name'})
        self.fields['coupon_code'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Coupon Code'})