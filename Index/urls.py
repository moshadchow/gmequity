from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.aboutUs,name='about'),
    path('partner/', views.gmPartner,name='partner'),
    path('approach-single/<int:id>/', views.approachSingle,name='approach-single'),
    path('service-single/<int:id>/', views.serviceSingle,name='service-single'),
    path('strategy-single/<int:id>/', views.strategySingle,name='strategy-single'),
    path('fund-info', views.fundInfo,name='fund-info'),
    path('fund-protect', views.fundProtect,name='fund-protect'),
    path('faq', views.faqs,name='faq'),
    path('goal', views.companyGoal,name='goal'),
    path('board-member', views.boardMember,name='board-member'),
    path('sip', views.sipRecord,name='sip'),
    path('news', views.companyNews,name='news'),
    path('tax', views.companyTax,name='tax'),
]