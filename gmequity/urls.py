from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Index.urls')),
    path('ContactUs/', include('Contact.urls')),
    path('Regulator/', include('Regulator.urls')),
    path('Download/', include('Download.urls')),
    path('Authentcation/', include('Authentication.urls')),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
