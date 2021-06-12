from django.conf.urls import url
from django.urls import path

from escola.views import  home

urlpatterns = [
     path('', views.home, name='home'),
]
