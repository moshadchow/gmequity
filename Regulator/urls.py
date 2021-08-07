from Index.models import partner
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Regulator,name='regulator')
]