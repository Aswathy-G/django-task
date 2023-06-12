from django.contrib import admin
from web.models import Product,Category


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("id","image","price","description")

admin.site.register(Product, PurchaseAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","title")

admin.site.register(Category, CategoryAdmin)
