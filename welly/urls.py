from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('analisis/', include('analisis.urls')),
    path('about/', include('about.urls')),
]
