from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return HttpResponse("Hello World")
    # context = {
    #     "title" : "Home Page"
    # }
    # return render(request,'web/index.html',context=context)

