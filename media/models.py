from django.db import models
from inventory.models import ProductInventory

class Media(models.Model):
    # Use the proper import and reference
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)
    # If you renamed img_url to image:
    image = models.ImageField(upload_to='products/images/' , default= 'products/images/placeholder.jpg')
    alt_text = models.CharField(max_length=255)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Media for {self.product_inventory.product.name}"