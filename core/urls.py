from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path('', include('app.urls')),
    path('api/', api.urls),
    path('admin/', admin.site.urls)
]
