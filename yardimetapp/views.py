from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'index.html')

def hakkimizda(request):
    return render(request,'hak.html')
    
def iletisim(request):
    return render(request,'iletisim.html')

