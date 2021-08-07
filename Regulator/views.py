from django.shortcuts import render
from .models import regulator

# Create your views here.
def Regulator(request):
    regulatordata = regulator.objects.all()
    context = {
        "regulators": regulatordata
    }
    return render(request,'regulator.html',context)
