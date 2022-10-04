
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('newproject.urls')),
    # path('api/v1/drf-auth/',include('rest_framework.urls')),
    # path('api/v1/auth/',include('djoser.urls')),
    # re_path(r'api/v1/',include('djoser.urls.authtoken'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
