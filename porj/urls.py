
from django.contrib import admin
from django.urls import path, include
from myproj import urls
from rest_framework import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myproj.urls')),
    path('api-auth/', include('rest_framework.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)