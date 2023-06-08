from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to="products/")
    name =  models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField()
    is_delete = models.BooleanField(default = False)
    is_edit = models.BooleanField(default = False)
    

    def __str__ (self):
        return self.name
   
    

