from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def store(request):
    data = {}
    if(request.POST['senha'] != request.POST['senha-conf']):
        data['msg'] = 'Senha e confirmação de senhas diferentes!'
        data['class'] = 'alert-danger'
    return render(request, 'cadastro.html', data)