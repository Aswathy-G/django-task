# Generated by Django 4.2.2 on 2023-06-12 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_remove_product_category_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='category',
        ),
    ]
