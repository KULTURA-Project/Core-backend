# products/management/commands/populate_product_data.py
import random
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from products.models import Category, ProductType, ProductAttribute, ProductAttributeValue



class Command(BaseCommand):
    help = 'Populate the database with product categories, types, attributes, and values'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate database...'))
        
        # Example categories
        categories = [
            'Paintings', 'Sculptures', 'Textiles', 'Wood Carvings', 'Jewelry'
        ]
        
        # Create categories
        for category_name in categories:
            slug = slugify(category_name)
            # Check if a category with the same slug already exists
            existing_category = Category.objects.filter(slug=slug).first()
            if existing_category:
                self.stdout.write(self.style.WARNING(f'Category "{category_name}" already exists'))
                continue
            
            category, created = Category.objects.get_or_create(
                name=category_name,
                slug=slug
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Category "{category_name}" created'))
        
        # Create subcategories (children)
        subcategories = [
            {'parent_slug': 'paintings', 'name': 'Abstract Paintings'},
            {'parent_slug': 'sculptures', 'name': 'Wood Sculptures'},
            {'parent_slug': 'textiles', 'name': 'African Prints'},
        ]
        
        for subcategory in subcategories:
            parent_category = Category.objects.filter(slug=subcategory['parent_slug']).first()
            if not parent_category:
                self.stdout.write(self.style.WARNING(f'Parent category "{subcategory["parent_slug"]}" not found'))
                continue
            
            slug = slugify(subcategory['name'])
            existing_subcategory = Category.objects.filter(slug=slug).first()
            if existing_subcategory:
                self.stdout.write(self.style.WARNING(f'Subcategory "{subcategory["name"]}" already exists'))
                continue
            
            subcategory_obj, created = Category.objects.get_or_create(
                name=subcategory['name'],
                slug=slug,
                parent=parent_category
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Subcategory "{subcategory["name"]}" created'))
        
        # Example product types
        product_types = [
            'Contemporary', 'Traditional', 'Abstract', 'Realistic'
        ]
        
        # Create product types
        for product_type_name in product_types:
            product_type, created = ProductType.objects.get_or_create(name=product_type_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Product Type "{product_type_name}" created'))
        
        # Example product attributes
        attributes = [
            {'name': 'Material', 'product_type': ProductType.objects.get(name='Contemporary')},
            {'name': 'Style', 'product_type': ProductType.objects.get(name='Traditional')},
            {'name': 'Color', 'product_type': ProductType.objects.get(name='Abstract')},
        ]
        
        # Create product attributes
        for attribute in attributes:
            attribute_obj, created = ProductAttribute.objects.get_or_create(
                name=attribute['name'],
                product_type=attribute['product_type']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Attribute "{attribute["name"]}" created'))
        
        # Example attribute values
        attribute_values = [
            {'product_attribute': ProductAttribute.objects.get(name='Material'), 'value': 'Wood'},
            {'product_attribute': ProductAttribute.objects.get(name='Style'), 'value': 'Modern'},
            {'product_attribute': ProductAttribute.objects.get(name='Color'), 'value': 'Blue'},
        ]

        # Create attribute values
        for value in attribute_values:
            value_obj, created = ProductAttributeValue.objects.get_or_create(
                product_attribute=value['product_attribute'],
                value=value['value']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Attribute Value "{value["value"]}" created'))
            
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
