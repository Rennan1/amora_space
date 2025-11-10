from django.contrib import admin
from .models import Fotografia

class ListarFotografias(admin.ModelAdmin):
    list_display = ("id","nome", "legenda", "categoria")
    list_display_links = ("id" ,"nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)

# Register your models here.
admin.site.register(Fotografia, ListarFotografias)