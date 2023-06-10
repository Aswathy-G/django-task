from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to="products/images")
    name =  models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField()
    is_deleted = models.BooleanField(default = False)
    is_edit = models.BooleanField(default = False)
    

    def __str__ (self):
        return self.name
   
   
class Category(models.Model):
    title = models.CharField(max_length=255)


    def __str__ (self):
        return self.title 
    

