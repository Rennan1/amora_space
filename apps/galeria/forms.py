from django import forms
from .models import Fotografia

class FotografiaForms(forms.ModelForm):

    class Meta:
        model = Fotografia
        exclude = ['publicada', 'usuario']
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data fotografia'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                },
                format='%Y-%m-%d'
            ),
        }