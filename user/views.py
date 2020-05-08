from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from yardimtalepler.models import yardimlar

# Create your views here.

def giris(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request,user)
            messages.add_message(request, messages.SUCCESS, 'Başarılı bir şekilde giriş yaptınız.')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR ,'Kullanıcı adı ya da parola hatalı. Tekrar deneyiniz.')
            return redirect('giris')
    else:

        return render(request,'user/giris.html')


def kayit(request):
    if request.method == 'POST':
        #user kayıt
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mail = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING ,'Kullanıcı adı daha önce alınmış. ')
                return redirect('kayit')
            else:
                if User.objects.filter(email = mail).exists():
                    messages.add_message(request, messages.WARNING ,'Mail adresi ile daha önce kayıt olunmuş. Lütfen başka bir mail adresi deneyiniz.')
                    return redirect('kayit')
                else:
                    user=User.objects.create_user(username=username, email=mail, password=password, first_name=firstname, last_name=lastname)
                    user.save()
                    messages.add_message(request, messages.SUCCESS ,'Kayıt işleminiz başarılı bir şekilde gerçekleşti.')
                    return redirect('giris')
        else:
            messages.add_message(request, messages.ERROR ,'Girdiğiniz parolalar eşleşmiyor. Tekrar deneyiniz.')
            return redirect('kayit')
    else:
        return render(request,'user/kayit.html')


def cikis(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS ,'Oturumdan güvenli bir şekilde çıkış yapıldı.')
        return redirect('index')
    else:
        return render(request,'user/cikis.html')

def hesap(request):
    if request.method == 'POST':
        user_id = request.POST['userid']
        users = User.objects.filter(id=user_id)
        context = {

            'users'    : users
        }
        return render(request, 'user/hesap.html',context)
    else:
        return render(request,'index.html')

def hesapyardimlar(request):
    if request.method == 'POST':
        user_id = request.POST['userid']
        yardimlars = yardimlar.objects.filter(userid=user_id)
        context= {

            'yardimlar' : yardimlars
        }

        return render(request,'user/hesapyardimlar.html', context)
    else:
        return render(request,'index.html')

def parola(request):
    if request.method == 'POST':    
        password = request.POST['yeni']
        user_id = request.POST['userid']
        print(password)
        User.objects.filter(id=user_id).update(password=password)
        messages.add_message(request, messages.SUCCESS ,'Parolanız başarıyla değiştirildi.')
        return render(request ,'index.html')
    else:   
        return render(request,'user/parola.html')

                