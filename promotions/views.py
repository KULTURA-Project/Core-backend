# promotions/views.py
from django.shortcuts import render
from .models import Promotion
from .forms import  PromotionForm
from django.shortcuts import render, redirect

def promotion_list(request):
    promotions = Promotion.objects.all()
    return render(request, 'promotions/promotion_list.html', {'promotions': promotions})

def add_promotion(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promotions:promotion_list')
    else:
        form = PromotionForm()
    return render(request, 'promotions/add_promotion.html', {'form': form})

def edit_promotion(request, pk):
    promotion = Promotion.objects.get(pk=pk)
    if request.method == 'POST':
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            form.save()
            return redirect('promotions:promotion_list')
    else:
        form = PromotionForm(instance=promotion)
    return render(request, 'promotions/edit_promotion.html', {'form': form})

def delete_promotion(request, pk):
    promotion = Promotion.objects.get(pk=pk)
    if request.method == 'POST':
        promotion.delete()
        return redirect('promotions:promotion_list')
    return render(request, 'promotions/delete_promotion.html', {'promotion': promotion})




# promotions/views.py
from django.shortcuts import render, redirect
from .forms import CouponForm
from .models import Coupon

def coupon_list(request):
    coupons = Coupon.objects.all()
    return render(request, 'promotions/coupon_list.html', {'coupons': coupons})

def add_coupon(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promotions:coupon_list')
    else:
        form = CouponForm()
    return render(request, 'promotions/add_coupon.html', {'form': form})

def edit_coupon(request, pk):
    coupon = Coupon.objects.get(pk=pk)
    if request.method == 'POST':
        form = CouponForm(request.POST, instance=coupon)
        if form.is_valid():
            form.save()
            return redirect('promotions:coupon_list')
    else:
        form = CouponForm(instance=coupon)
    return render(request, 'promotions/edit_coupon.html', {'form': form})

def delete_coupon(request, pk):
    coupon = Coupon.objects.get(pk=pk)
    if request.method == 'POST':
        coupon.delete()
        return redirect('promotions:coupon_list')
    return render(request, 'promotions/delete_coupon.html', {'coupon': coupon})
