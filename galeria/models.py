from django.db import models

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
    foto = models.CharField(max_length=100)

    def __str__(self):
        return self.nome