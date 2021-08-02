from django.shortcuts import render
from . models import about
from . models import slider
from . models import client
from . models import category
from . models import product

# Create your views here.


def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    categorydata = category.objects.all()
    productdata = product.objects.all()
    print(category)
    context = {
        "about": aboutdata,
        "slider": sliderdata,
        "client": clientdata,
        "categories": categorydata,
        "products": productdata
    }
    return render(request, "index.html", context)


def aboutus(request):
    return render(request, "about.html")
