# products/views.py
from django.shortcuts import render, redirect
from .models import Product, Category, ProductType
from .forms import ( 
                    ProductForm , ProductInventoryForm  ,MediaForm,
                    PromotionForm , ProductPromoForm
                    )  
# products/views.py
from django.shortcuts import render, redirect
from .forms import ProductAttributeForm, PromotionForm, ProductPromoForm, MediaForm  , CategoryForm
from promotions.models import ProductPromo , Promotion 
from django.shortcuts import render, redirect
from .forms import ProductForm, ProductInventoryForm
from .models import Product
from django.contrib import messages
from media.models import Media
from inventory.models import  ProductInventory
from django.shortcuts import render
from django.forms import inlineformset_factory
from .forms import ProductForm, PromotionForm, ProductPromoForm, MediaForm
from .models import Category, ProductType, ProductAttribute, ProductAttributeValue, ProductTypeAttribute  




from django.http import JsonResponse
from .models import ProductAttribute

def fetch_product_attributes(request, product_type_id):
    attributes = ProductAttribute.objects.filter(product_type_id=product_type_id)
    attribute_list = [{'id': attr.id, 'name': attr.name} for attr in attributes]
    return JsonResponse({'attributes': attribute_list})


def get_subcategories(request):
    if request.method == 'POST':
        category_id = request.POST.get('categoryId')
        subcategories = Category.objects.filter(parent_id=category_id)
        data = [{'id': sc.id, 'name': sc.name} for sc in subcategories]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)






'''def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        inventory_form = ProductInventoryForm(request.POST)
        media_form = MediaForm(request.POST, request.FILES)

        # Handling attributes dynamically
        attribute_forms = []
        selected_product_type = request.POST.get('product_type')
        
        if selected_product_type:
            product_type = ProductType.objects.get(id=selected_product_type)
            attributes = ProductAttribute.objects.filter(product_type=product_type)
            for attribute in attributes:
                # Create a form for each attribute value
                attribute_form = ProductAttributeValueForm(initial={'attribute': attribute})
                attribute_forms.append(attribute_form)

        if product_form.is_valid() and inventory_form.is_valid() and media_form.is_valid():
            # Save the product and its related data
            product = product_form.save()
            inventory = inventory_form.save(commit=False)
            inventory.product = product
            inventory.save()

            # Save the media
            media = media_form.save(commit=False)
            media.product = product
            media.save()

            # Save attribute values
            for attribute_form in attribute_forms:
                if attribute_form.is_valid():
                    attribute_value = attribute_form.save(commit=False)
                    attribute_value.product = product
                    attribute_value.save()

            return redirect('product_list')  # Redirect after saving
    else:
        product_form = ProductForm()
        inventory_form = ProductInventoryForm()
        media_form = MediaForm()

        # Default list of attribute forms (empty)
        attribute_forms = []

    return render(request, 'products/add_product.html', {
        'product_form': product_form,
        'inventory_form': inventory_form,
        'media_form': media_form,
        'attribute_forms': attribute_forms,
    })'''
    
    
def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        
        # Handle media forms dynamically (if you have multiple media forms)
        media_forms = [MediaForm(request.POST, request.FILES, prefix=f'media_{i}') for i in range(3)]  # 3 media forms

        if product_form.is_valid():
            # Save the product form
            product = product_form.save()
            
            # Process each media form if it's valid
            for media_form in media_forms:
                if media_form.is_valid():
                    media_instance = media_form.save(commit=False)
                    media_instance.product = product  # Associate media with the product
                    media_instance.save()

            # Redirect after successful form submission
            return redirect('/admin')  # Change 'product_list' to the appropriate URL name

    else:
        product_form = ProductForm()
        media_forms = [MediaForm(prefix=f'media_{i}') for i in range(3)]  # Empty media forms for GET request

    # Fetch product attributes dynamically based on the product type or other logic
    product_attributes = ProductAttribute.objects.all()  # Adjust this to fetch attributes based on product type

    return render(request, 'products/add_product.html', {
        'form': product_form,
        'media_forms': media_forms,
        'product_attributes': product_attributes,
    }) 
    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})    
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
