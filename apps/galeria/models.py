from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Fotografia(models.Model):

    categorias = [
        ('DIÁRIA', "Diária"),
        ('PASSEIO', "Passeio"),
        ('CASA', "Casa"),
        ('OUTROS', "Outros")

    ]

    nome = models.CharField(max_length=100)
    legenda = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100, choices=categorias, default ='')
    descricao = models.TextField(blank=True)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateField(default=date.today)
    usuario = models.ForeignKey( # Relação de muitos para um com o modelo User
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='usuario'
    )

    def __str__(self):
        return self.nome