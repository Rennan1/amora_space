from django import forms

class LoginForms(forms.Form):

    usuario=forms.CharField(
    label='Nome de usuário', 
    required=True, 
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: joaozinho123',
        }
    )
    )
    senha=forms.CharField(
    label='Senha', 
    required=True, 
    max_length=70,
    widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
        }
    ),
    )

class CadastroForms(forms.Form):
    usuario=forms.CharField(
    label='Nome de usuário', 
    required=True, 
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: joaozinho123',
        }
    )
    )
    email=forms.EmailField(
    label='E-mail', 
    required=True, 
    max_length=100,
    widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: email@exemplo.com',
        }
    )
    )
    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )
    senha_2=forms.CharField(
        label='Confirme sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha',
            }
        ),
    )