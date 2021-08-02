from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Index.urls')),
    path('AboutUs/', include('About.urls')),
    path('ContactUs/', include('Contact.urls')),
    path('ProfilePage/', include('Employee.urls')),
    path('Authentcation/', include('Authentication.urls')),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
