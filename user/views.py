from pydoc import describe
from django.shortcuts import render
from .models import Pessoa

def userHome(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'user.html', {"pessoas":pessoas})

def salvar(request):
    vnome = request.POST.get('nome')
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    return render(request, 'user.html', {'pessoas': pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'udpate.html', {'pessoa': pessoa})