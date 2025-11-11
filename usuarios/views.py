from django.shortcuts import render, redirect
from .forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            usuario = form['usuario'].value()
            senha = form['senha'].value()

        user = auth.authenticate(request, username=usuario, password=senha)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form' : form})

def cadastro(request):    
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value(): #verifica se as senhas são iguais
                return redirect('cadastro')

            usuario=form["usuario"].value() #pega o valor do campo nome_cadastro
            email=form["email"].value() #pega o valor do campo email
            senha=form["senha_1"].value() #pega o valor do campo senha_1

            if User.objects.filter(username=usuario).exists():
                return redirect('cadastro')
            
            cadastro = User.objects.create_user(
                username = usuario,
                email = email,
                password = senha
            )
            cadastro.save()
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form' : form})