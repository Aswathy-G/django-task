from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

from web.models import Product,Category




def index(request):
    products = Product.objects.filter(is_deleted=False,is_edit=False)

    instances = Paginator(products,6)
    page = request.GET.get('page',1)
    try:
        instances = instances.page(page)
    except PageNotAnInteger:
        instances = instances.page(1)
    except EmptyPage:
        instances = instances.page(instances.num_pages)

    categorys = Category.objects.all()

    context={
        "title":"HomePage",
        "instances" : instances,
         "categorys":categorys
        }
    return render(request,'index.html',context=context)

    
   

