from django.db import models
from inventory.models import ProductInventory

class PromoType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    name = models.CharField(max_length=255)
    coupon_code = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    promo_product = models.ManyToManyField(ProductInventory, through='ProductPromo')  # Many-to-Many relationship
    promo_reduction = models.DecimalField(max_digits=5, decimal_places=2)
    coupon = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.SET_NULL)
    promo_start = models.DateTimeField()
    time_end = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_scheduled = models.BooleanField(default=False)
    promo_type = models.ForeignKey(PromoType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductPromo(models.Model):
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)  # Correct field name
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)  # Correct field name
    price_override = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional
    promo_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional

    class Meta:
        unique_together = (('product_inventory', 'promotion'),)  # Prevent duplicate promotions for the same product

    def __str__(self):
        return f"{self.product_inventory.sku} - {self.promotion.name}"
