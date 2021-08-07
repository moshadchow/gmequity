from django.shortcuts import render
from .models import about
from .models import slider
from .models import partner
from .models import advisor
from .models import category
from .models import product

# Create your views here.


def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    partnerdata = partner.objects.all()
    categorydata = category.objects.all()
    productdata = product.objects.all()
    advisorlist = advisor.objects.all()
    context = {
        "about": aboutdata,
        "sliders": sliderdata,
        "partners": partnerdata,
        "categories": categorydata,
        "products": productdata,
        "advisors" : advisorlist
    }
    return render(request, "index.html", context)


def aboutus(request):
    aboutdata = about.objects.all()[0]
    context = {
        "abouts": aboutdata
    }
    return render(request, "about.html",context)

def gmpartner(request):
    partnerdata = partner.objects.all()
    context = {
        "partners": partnerdata
    }
    return render(request,'partner.html',context)
