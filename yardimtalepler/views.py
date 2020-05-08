from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import yardimlar
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def index(request):
    yardimtaleps = yardimlar.objects.all()
    context={
        'yardimlar' : yardimtaleps
    }
    return render(request , 'yardimtalepler/yardimlist.html' , context)

def detail(request, yardimlar_id):
    if request.method == 'POST':
            durum = 0

            yardimlar.objects.filter(id=yardimlar_id).update(durum=durum)
            messages.add_message(request, messages.SUCCESS ,'Yardım talebine cevap verdiğiniz için TEŞEKKÜR EDERİZ.')
            return render(request ,'index.html')
    else:    
        yardims = get_object_or_404(yardimlar , pk = yardimlar_id)
        context = {

            'yardimlar' : yardims,

        }
        

        return render(request,'yardimtalepler/detail.html',context)

def ara(request):
    return render(request,'yardimtalepler/ara.html')



def yardimtalepet(request):
    if request.method == 'POST':
        #yardim kayıt
        
        user_id = request.POST['userid']
        baslik1 = request.POST['baslik']
        aciklama1 = request.POST['aciklama']
        adres1 = request.POST['adres']
        telefon1 = request.POST['telefon']
        resim1 = request.FILES['resim']
        ufirstname1 = request.POST['userfirst']
        ulastname1  = request.POST['userlast']
        uemail1  = request.POST['usermail']
        
        yardim=yardimlar(baslik = baslik1,aciklama = aciklama1, adres = adres1 , telefon = telefon1 ,resim = resim1 , userid=user_id , u_firstname=ufirstname1 , u_lastname=ulastname1, u_email = uemail1)
        yardim.save()
        messages.add_message(request, messages.SUCCESS ,'Kayıt işleminiz başarılı bir şekilde gerçekleşti.')


        return render(request ,'index.html')
    else:
        return render(request,'yardimtalepet.html')



        
