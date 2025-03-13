from django.db import models


class ProductInventory(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    upc = models.CharField(max_length=255, unique=True, null=True, blank=True)
    product_type = models.ForeignKey('products.ProductType', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    store_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_digital = models.BooleanField(default=False)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordering = models.PositiveIntegerField(default=0, db_index=True)
    class Meta:
        ordering = ['created_at']
class ProductAttributeValues(models.Model):
    attribute_value = models.ForeignKey('products.ProductAttributeValue', on_delete=models.CASCADE , related_name='values'
)
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)

