from .models import download
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Download,name='download')
]