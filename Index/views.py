from django.shortcuts import render
from .models import about, fund_info, fund_protect
from .models import service
from .models import strategy
from .models import slider
from .models import partner
from .models import advisor
from .models import approach

# Create your views here.


def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    partnerdata = partner.objects.all()
    advisorlist = advisor.objects.all()
    approachlist = approach.objects.all()
    servicelist = service.objects.all()
    strategylist = strategy.objects.all()
    context = {
        "about": aboutdata,
        "sliders": sliderdata,
        "partners": partnerdata,
        "advisors" : advisorlist,
        "approaches" : approachlist,
        "services" : servicelist,
        "strategies" : strategylist
    }
    return render(request, "index.html", context)


def aboutUs(request):
    aboutdata = about.objects.all()[0]
    context = {
        "abouts": aboutdata
    }
    return render(request, "about.html",context)

def gmPartner(request):
    partnerdata = partner.objects.all()
    context = {
        "partners": partnerdata
    }
    return render(request,'partner.html',context)

def approachSingle(request,id):
    all_approach = approach.objects.all()
    approach_single = approach.objects.filter(pk = id)[0]
    context = {'approaches': all_approach , 'approach': approach_single }
    return render(request,'approach-single.html',context)

def serviceSingle(request,id):
    all_service = service.objects.all()
    service_single = service.objects.filter(pk = id)[0]
    context = {'services': all_service , 'service': service_single }
    return render(request,'service-single.html',context)

def strategySingle(request,id):
    all_strategy = strategy.objects.all()
    strategy_single = strategy.objects.filter(pk = id)[0]
    context = {'strategies': all_strategy , 'strategy': strategy_single }
    print (strategy_single)
    return render(request,'strategy-single.html',context)

def fundInfo(request):
    fund_Information = fund_info.objects.all()[0]
    context = {
        "fund_info": fund_Information
    }
    return render(request,'fund-info.html',context)

def fundProtect(request):
    fund_Protection = fund_protect.objects.all()[0]
    context = {
        "fund_protect": fund_Protection
    }
    return render(request,'fund-protect.html',context)