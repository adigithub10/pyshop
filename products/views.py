from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# creating a view function
def index(request):
   products = Product.objects.all()
   return render(request,'index.html' ,
                  {'products':products})


def new (request):
   return HttpResponse("Heyy!! welcome to new page")