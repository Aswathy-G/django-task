from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from posts.forms import ProductForm


@login_required(login_url="users/login/")
def create_post(request):
       context = {
           "title": "Create new post"
           
       }
       return render(request, "posts/create.html", context=context)