from django.shortcuts import render, get_object_or_404, redirect
from .models import Fotografia
from .forms import FotografiaForms
from django.contrib import messages
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'É necessário estar autenticado para visitar a tela inicial.') 
        return redirect('login')
    fotografias = Fotografia.objects.filter(publicada=True).order_by('-data_fotografia') # usuario=request.user  # para cada usuário ver apenas suas fotos
    return render(request, 'galeria/index.html', {"fotografias": fotografias})

def imagem(request, fotografia_id):
    if not request.user.is_authenticated:
        messages.error(request, 'É necessário estar autenticado para visualizar uma imagem.') 
        return redirect('login')
    
    fotografia = get_object_or_404(Fotografia, id=fotografia_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'É necessário estar autenticado para realizar uma busca.')
        return redirect('login')
    fotografias = Fotografia.objects.filter(publicada=True).order_by('-data_fotografia')

    nome_a_buscar = request.GET.get('buscar', '').strip()
    if nome_a_buscar:
        fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/index.html', {"fotografias": fotografias})

def nova_imagem(request):
      # Apenas superusuário pode acessar
    if not request.user.is_superuser:
        messages.error(request, 'Apenas pessoas autorizadas podem adicionar novas imagens.')
        return redirect('index')
    
    form = FotografiaForms

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, fotografia_id):
    fotografia = Fotografia.objects.get(id=fotografia_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'galeria/editar_imagem.html', {'form': form,'fotografia': fotografia})

def deletar_imagem(request, fotografia_id):
    fotografia = Fotografia.objects.get(id=fotografia_id)
    fotografia.delete()
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.filter(publicada=True, categoria=categoria).order_by('-data_fotografia')

    return render(request, 'galeria/index.html', {'fotografias': fotografias})