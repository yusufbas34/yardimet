from django.contrib import admin
from .models import yardimlar
# Register your models here.
class YardimAdmin(admin.ModelAdmin):
    list_display=('id','baslik','zaman','durum')
    list_display_links=('id','baslik')
    list_filter=('baslik','durum')
    search_fields=('baslik','durum')
    list_per_page=20

admin.site.register(yardimlar,YardimAdmin)