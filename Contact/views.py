from django.shortcuts import render
# from .models import contact
from .forms import contactForm
from django.core.mail import send_mail

def contactus(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            fromemail = form.cleaned_data['fromemail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject,message,fromemail,['moshad@sheltechbrokerage.com'])
    else:
        form = contactForm()
    return render(request,'contact.html',{'form':form})