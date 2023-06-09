from django.shortcuts import render
from django.http.response import HttpResponse

from web.models import Product,Category




def index(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context={
        "products":products,
         "categorys":categorys
        }
    return render(request,'index.html',context=context)

    
   

