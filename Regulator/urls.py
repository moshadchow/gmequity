from .models import regulator
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Regulator,name='regulator')
]