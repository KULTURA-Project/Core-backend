from django.db import models
from django.utils.text import slugify
import uuid
from datetime import datetime
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

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
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Auto-generate slug if not provided
        if not self.slug:
            self.slug = self._generate_unique_slug()
        
        # Auto-generate web_id if not provided
        if not self.web_id:
            self.web_id = self._generate_unique_web_id()
            
        super().save(*args, **kwargs)
    
    def _generate_unique_slug(self):
        """Generate a unique slug based on product name"""
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        
        # Keep checking until we have a unique slug
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
            
        return unique_slug
    
    def _generate_unique_web_id(self):
        """Generate a unique web_id based on date, category, and UUID"""
        # Format: CAT-YYYYMMDD-XXXX where XXXX is a short unique string
        today = datetime.now().strftime('%Y%m%d')
        
        # Get category prefix (first 3 letters of category name, uppercase)
        category_prefix = self.category.name[:3].upper() if self.category else "PRD"
        
        # Get a short unique string (first 8 chars of a UUID)
        unique_id = str(uuid.uuid4())[:8]
        
        web_id = f"{category_prefix}-{today}-{unique_id}"
        
        # Ensure the web_id is unique by checking the database
        while Product.objects.filter(web_id=web_id).exists():
            unique_id = str(uuid.uuid4())[:8]
            web_id = f"{category_prefix}-{today}-{unique_id}"
        
        return web_id

    def __str__(self):
        return self.name
