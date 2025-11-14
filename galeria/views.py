from django.shortcuts import render, get_object_or_404, redirect
from .models import Fotografia
from django.contrib import messages
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'É necessário estar autenticado para visitar a tela inicial.') # usuario=request.user  # para cada usuário ver apenas suas fotos
        return redirect('login')
    fotografias = Fotografia.objects.filter(publicada=True).order_by('-data_fotografia') 
    return render(request, 'galeria/index.html', {"fotografias": fotografias})

def imagem(request, fotografia_id):
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

    return render(request, 'galeria/buscar.html', {"fotografias": fotografias})