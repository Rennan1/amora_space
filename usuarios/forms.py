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

    def clean_usuario(self):
        nome = self.cleaned_data.get('usuario')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo")
            else:
                return nome

    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas precisam ser iguais')
            else:
                return senha_2