from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductAttribute(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    attribute_value = models.TextField()

    def __str__(self):
        return f"{self.product_attribute.name}: {self.attribute_value}"

class ProductTypeAttribute(models.Model):
    product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_type.name} - {self.product_attribute.name}"

class Product(models.Model):
    web_id = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True, blank=True, related_name='products') # Associate ProductType with Product
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
