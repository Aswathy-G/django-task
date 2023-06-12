from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
from web.forms import ProductForm

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
    return render(request,'web/index.html',context=context)


def create_product(request):
    # print("first")
    if request.method == 'POST':
        # print("second")
        form = ProductForm(request.POST,request.FILES)
        

        if form.is_valid():
            # print("hai")
            form.save()
            # return redirect('web/index.html')  # Redirect to the product list page
            return HttpResponseRedirect(reverse('web:index'))
    else:
        form = ProductForm()

        return render(request, 'web/create.html', {'form': form})

   

