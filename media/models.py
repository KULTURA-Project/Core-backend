# media/models.py
from django.db import models
from products.models import Product  # Ensure Product is imported
from inventory.models import ProductInventory

class Media(models.Model):
    # ForeignKey to Product
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media_set')
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/', default='products/images/placeholder.jpg')
    alt_text = models.CharField(max_length=255)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Media for {self.product.name}"
