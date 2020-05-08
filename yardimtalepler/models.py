from django.db import models

# Create your models here.


class yardimlar(models.Model):
    baslik = models.CharField(max_length=100, verbose_name="Yardım Başlığı")
    aciklama = models.TextField(verbose_name="Yardım Açıklaması")
    adres = models.TextField(null=True)
    telefon = models.CharField(max_length=10,null=True)
    resim = models.FileField(null=True, blank=True)
    zaman = models.DateTimeField(auto_now_add=True)
    durum = models.BooleanField(default=True)
    userid = models.TextField(null=True)
    u_firstname= models.CharField(max_length=20,null=True)
    u_lastname= models.CharField(max_length=20,null=True)
    u_email= models.CharField(max_length=20,null=True)


    def __str__(self):
        return self.baslik

    def get_image_path(self):
        return '/img/'+ self.resim