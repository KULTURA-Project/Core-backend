from django.db import models
from inventory.models import ProductInventory

class Media(models.Model):
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)
    img_url = models.URLField()
    alt_text = models.CharField(max_length=255)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alt_text
