from django import forms
from django.forms.widgets import MediaDefiningClass

class contactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name','class':'form-control'}),required=True)
    fromemail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control'}),required=True)
    subject =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject','class':'form-control'}),required=True)
    message =  forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message','class':'form-control'}),required=True)