from django.shortcuts import render, get_object_or_404
from .models import Fotografia
# Create your views here.

def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"fotografias": fotografias})

def imagem(request, fotografia_id):
    fotografia = get_object_or_404(Fotografia, id=fotografia_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})