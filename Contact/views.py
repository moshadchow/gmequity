from django.shortcuts import render
from .models import contact

def contactus(request):
    return render(request,'contact.html')