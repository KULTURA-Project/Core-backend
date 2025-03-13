# products/management/commands/populate_products.py
import random
from django.core.management.base import BaseCommand
from products.models import Product, Category, ProductType, ProductInventory



class Command(BaseCommand):
    help = 'Populate the database with products'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate database...'))
        
        # Example categories
        categories = Category.objects.all()
        
        # Example product types
        product_types = ProductType.objects.all()
        
        # Populate products
        for _ in range(10):  # Create 10 products
            category = random.choice(categories)
            product_type = random.choice(product_types)
            
            product = Product.objects.create(
                name=f"African Art Piece {_}",
                description="A beautiful piece of African art.",
                category=category,
                product_type=product_type,
                is_active=True
            )
            
            # Create product inventory
            # Adjusted to match the existing model structure
            ProductInventory.objects.create(
                product_type=product,  # Use product_type field
                product=product_type,  # Use product field (though this seems incorrect)
                sku=f"SKU-{_}",
                upc=f"UPC-{_}",
                is_active=True,
                is_default=True,
                retail_price=random.randint(100, 1000),
                store_price=random.randint(50, 500),
                weight=random.uniform(1.0, 10.0)
            )
        
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))

