from django.contrib import admin
from web.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","image","name","price","description")

admin.site.register(Product, ProductAdmin)
