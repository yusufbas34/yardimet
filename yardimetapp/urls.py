from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda', views.hakkimizda , name='hakkimizda'), 
    path('iletisim', views.iletisim , name='iletisim'), 
  ]