from django.contrib import admin
from .models import Fotografia

class ListarFotografias(admin.ModelAdmin):
    list_display = ("id","nome", "legenda", "categoria", "publicada") # definir quais colunas queremos na listagem
    list_display_links = ("id" ,"nome") # definir quais colunas serão "clicáveis" para exibir detalhes do item
    search_fields = ("nome",) # adicionar campo de busca e passar como parâmetro o campo que será utilizado para busca (precisa ser tupla)
    list_filter = ("categoria", "publicada", "usuario")
    list_editable = ("publicada",) # editar através da listagem
    list_per_page = 10

# Register your models here.
admin.site.register(Fotografia, ListarFotografias)