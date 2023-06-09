from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to="products/images")
    category =  models.CharField(max_length=25)
    price = models.CharField(max_length=255)
    description = models.TextField()
    is_deleted = models.BooleanField(default = False)
    is_edit = models.BooleanField(default = False)
    

    def __str__ (self):
        return self.price
   
   
class Category(models.Model):
  
    title= models.CharField(max_length=255)


    def __str__ (self):
        return str(self.id)
    

