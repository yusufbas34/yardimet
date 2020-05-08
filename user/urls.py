from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('giris/', views.giris, name='giris'),
    path('kayit/', views.kayit, name='kayit'),
    path('cikis/', views.cikis, name='cikis'),
    path('hesap/', views.hesap, name='hesap'),
    path('parola/', views.parola, name='parola'),
    path('hesapyardimlar/', views.hesapyardimlar, name='hesapyardimlar'),

]