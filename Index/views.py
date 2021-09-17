from django.shortcuts import render
from .models import about, company_goal, fund_info, fund_protect,financial_info, news
from .models import service
from .models import strategy
from .models import slider
from .models import partner
from .models import advisor
from .models import approach
from .models import faq
from .models import company_goal
from .models import sip
from .models import board_member
from .models import news
from .models import tax
from .forms import contactForm
from django.core.mail import send_mail
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
           name = form.cleaned_data['name']
           fromemail = form.cleaned_data['fromemail']
           subject = form.cleaned_data['subject']
           message = form.cleaned_data['message']
           send_mail(subject,message,fromemail,['moshad@sheltechbrokerage.com'])
           
           aboutdata = about.objects.all()[0]
           sliderdata = slider.objects.all()
           partnerdata = partner.objects.all()
           board_mem = board_member.objects.all()
           approachlist = approach.objects.all()
           servicelist = service.objects.all()
           strategylist = strategy.objects.all()
           financial_Info = financial_info.objects.all()[0]
           form = contactForm()
           context = {
                "about": aboutdata,
                "sliders": sliderdata,
                "partners": partnerdata,
                "board_mem": board_mem,
                "approaches": approachlist,
                "services": servicelist,
                "strategies": strategylist,
                "financial" : financial_Info,
                "form" : form
            }
    else:
        aboutdata = about.objects.all()[0]
        sliderdata = slider.objects.all()
        partnerdata = partner.objects.all()
        board_mem = board_member.objects.all()
        approachlist = approach.objects.all()
        servicelist = service.objects.all()
        strategylist = strategy.objects.all()
        financial_Info = financial_info.objects.all()[0]
        form = contactForm()
        context = {
            "about": aboutdata,
            "sliders": sliderdata,
            "partners": partnerdata,
            "board_mem": board_mem,
            "approaches": approachlist,
            "services": servicelist,
            "strategies": strategylist,
            "financial" : financial_Info,
            "form" : form
        }
    return render(request, "index.html", context)


def aboutUs(request):
    aboutdata = about.objects.all()[0]
    context = {
        "about": aboutdata
    }
    return render(request, "about.html", context)


def gmPartner(request):
    partnerdata = partner.objects.all()
    context = {
        "partners": partnerdata
    }
    return render(request, 'partner.html', context)


def approachSingle(request, id):
    all_approach = approach.objects.all()
    approach_single = approach.objects.filter(pk=id)[0]
    context = {'approaches': all_approach, 'approach': approach_single}
    return render(request, 'approach-single.html', context)


def serviceSingle(request, id):
    all_service = service.objects.all()
    service_single = service.objects.filter(pk=id)[0]
    context = {'services': all_service, 'service': service_single}
    return render(request, 'service-single.html', context)


def strategySingle(request, id):
    all_strategy = strategy.objects.all()
    strategy_single = strategy.objects.filter(pk=id)[0]
    context = {'strategies': all_strategy, 'strategy': strategy_single}
    print(strategy_single)
    return render(request, 'strategy-single.html', context)


def fundInfo(request):
    fund_Information = fund_info.objects.all()[0]
    context = {
        "fund_info": fund_Information
    }
    return render(request, 'fund-info.html', context)


def fundProtect(request):
    fund_Protection = fund_protect.objects.all()[0]
    context = {
        "fund_protect": fund_Protection
    }
    return render(request, 'fund-protect.html', context)

def faqs(request):
    cus_query = faq.objects.all()
    context = {
        "cus_query": cus_query
    }
    return render(request, 'faq.html',context)

def companyGoal(request):
    com_goal = company_goal.objects.all()[0]
    context = {
        "com_goal": com_goal
    }
    return render(request, 'goal.html',context)

def sipRecord(request):
    siprecord = sip.objects.all()[0]
    context = {
        "sip_record": siprecord
    }
    return render(request, 'sip.html',context)

def boardMember(request):
    board_mem = board_member.objects.all()
    context = {
        "board_mem": board_mem
    }
    return render(request, 'board_member.html',context)

def companyNews(request):
    com_news = news.objects.all()[0]
    context = {
        "com_news": com_news
    }
    return render(request, 'news.html',context)

def companyTax(request):
    com_tax = tax.objects.all()[0]
    context = {
        "com_tax": com_tax
    }
    return render(request, 'tax.html',context)
