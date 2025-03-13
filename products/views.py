# products/views.py
from django.shortcuts import render, redirect
from .models import Product, Category, ProductType
from .forms import ( 
                    ProductForm , ProductInventoryForm  ,MediaForm,
                    PromotionForm , ProductPromoForm
                    )  
 
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        promotion_form = PromotionForm(request.POST)
        product_promo_form = ProductPromoForm(request.POST)
        
        if product_form.is_valid() and promotion_form.is_valid() and product_promo_form.is_valid():
            product = product_form.save()
            promotion = promotion_form.save()
            product_promo = product_promo_form.save(commit=False)
            product_promo.promotion = promotion
            # Assuming you have a way to get the ProductInventory instance
            # product_promo.product_inventory = product_inventory_instance
            product_promo.save()
            
            return redirect('products:product_list')
    else:
        product_form = ProductForm()
        promotion_form = PromotionForm()
        product_promo_form = ProductPromoForm()
    
    return render(request, 'products/add_product.html', {
        'product_form': product_form,
        'promotion_form': promotion_form,
        'product_promo_form': product_promo_form
    })

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/delete_product.html', {'product': product})
