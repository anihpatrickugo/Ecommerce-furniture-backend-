# Generated by Django 4.1.4 on 2023-01-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_remove_products_categories_products_categories"),
    ]

    operations = [
        migrations.RenameField(
            model_name="products", old_name="price", new_name="initial_price",
        ),
    ]
