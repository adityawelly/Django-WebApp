from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('crawling', views.crawling),
    path('preprocessing', views.preprocessing),
    path('classification', views.classification),
    path('visualization', views.visualization),
]