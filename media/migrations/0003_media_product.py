# Generated by Django 5.1.7 on 2025-03-13 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_remove_media_img_url_media_image'),
        ('products', '0004_productattribute_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='products.product'),
            preserve_default=False,
        ),
    ]
