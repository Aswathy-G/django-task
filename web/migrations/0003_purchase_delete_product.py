# Generated by Django 4.2.2 on 2023-06-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='purchases/images')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_delete', models.BooleanField(default=False)),
                ('is_edit', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
