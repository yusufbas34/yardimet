from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='yardimtalepler'),
    path('<int:yardimlar_id>', views.detail, name='detail'),
    path('ara', views.ara, name='ara'),
    path('yardimtalepet', views.yardimtalepet , name='yardimtalepet'),
]