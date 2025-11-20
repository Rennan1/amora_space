from django.shortcuts import render, redirect
from .forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    form = LoginForms()
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            usuario = form['usuario'].value()
            senha = form['senha'].value()

        user = auth.authenticate(request, username=usuario, password=senha) # autentica o usuario
        if user is not None: # se o usuario for valido
            auth.login(request, user)
            return redirect('index')
        else: # se o usuario for invalido
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form' : form})

def cadastro(request):    
    form = CadastroForms()

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            usuario=form["usuario"].value() #pega o valor do campo nome_cadastro
            email=form["email"].value() #pega o valor do campo email
            senha=form["senha_1"].value() #pega o valor do campo senha_1

            if User.objects.filter(username=usuario).exists(): # verifica se o usuario ja existe
                messages.error(request, 'Usuario ja cadastrado.')
                return redirect('cadastro')
            
            if User.objects.filter(email=email).exists(): # verifica se o usuario ja existe
                messages.error(request, 'Esse e-mail já está em uso.')
                return redirect('cadastro')
            
            cadastro = User.objects.create_user(
                username = usuario,
                email = email,
                password = senha
            )
            cadastro.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form' : form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')