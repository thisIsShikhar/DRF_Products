# Generated by Django 4.0.6 on 2023-01-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product_image_product_imgheight_product_imgwidth'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ProductInfo',
            field=models.TextField(blank=True, null=True),
        ),
    ]