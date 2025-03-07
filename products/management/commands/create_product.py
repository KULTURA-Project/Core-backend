from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category, ProductType, ProductAttribute, ProductAttributeValue
from inventory.models import ProductInventory, ProductAttributeValues
from media.models import Media
from promotions.models import Promotion, ProductPromo, PromoType, Coupon
from django.utils.text import slugify
import uuid

class Command(BaseCommand):
    help = 'Creates a full "art product" with associated details'

    def handle(self, *args, **options):
        # 1. Create Category
        category, created = Category.objects.get_or_create(
            name="Art",
            defaults={'slug': slugify("Art"), 'is_active': True}
        )

        # 2. Create ProductType
        product_type, created = ProductType.objects.get_or_create(name="Painting")

        # 3. Create Product
        product_name = "Unique Oil Painting"
        product, created = Product.objects.get_or_create(
            name=product_name,
            web_id=str(uuid.uuid4()),  # Generate a unique web_id
            defaults={
                'slug': slugify(product_name),
                'description': "A beautiful, one-of-a-kind oil painting.",
                'category': category,
                'product_type': product_type,
                'is_active': True
            }
        )

        # 4. Create ProductInventory
        inventory, created = ProductInventory.objects.get_or_create(
            sku="oil-painting-001",
            product=product,
            defaults={
                'upc': str(uuid.uuid4()),
                'product_type': product_type,
                'is_active': True,
                'is_default': True,
                'retail_price': 150.00,
                'store_price': 120.00,
                'is_digital': False,
                'weight': 1.0
            }
        )

        # 5. Create Media
        Media.objects.create(
            product_inventory=inventory,
            img_url="https://example.com/images/oil-painting.jpg",
            alt_text="Oil Painting",
            is_feature=True
        )

        # 6. Product Attributes (Example: Size)
        size_attribute, created = ProductAttribute.objects.get_or_create(
            name="Size",
            description="The size of the painting"
        )
        size_value, created = ProductAttributeValue.objects.get_or_create(
            product_attribute=size_attribute,
            attribute_value="24x36 inches"
        )

        #7. Linking Attribute Values to Inventory
        ProductAttributeValues.objects.create(
            product_inventory = inventory,
            attribute_value = size_value
        )

        # 8. Example Promotion
        promo_type, created = PromoType.objects.get_or_create(name="Discount")
        coupon, created = Coupon.objects.get_or_create(name="SummerSale", coupon_code="SUMMER20")
        promotion = Promotion.objects.create(
            name="Summer Sale 20% Off",
            description="20% off all art products this summer!",
            promo_reduction=20.00,
            coupon=coupon,
            promo_start="2025-06-01",
            time_end="2025-08-31",
            is_active=True,
            is_scheduled=False,
            promo_type=promo_type
        )

        ProductPromo.objects.create(
            product_inventory=inventory,
            promotion=promotion
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created art product: {product_name}'))
