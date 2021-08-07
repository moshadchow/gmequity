from django.shortcuts import render
from .models import download

# Create your views here.
def Download(request):
    downloaddata = download.objects.all()
    context = {
        "downloads": downloaddata
    }
    return render(request,'download.html',context)