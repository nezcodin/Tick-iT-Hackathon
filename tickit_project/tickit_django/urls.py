from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('tickit.frontend_urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('rest/', include('tickit.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
