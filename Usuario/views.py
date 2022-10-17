from audioop import reverse
from multiprocessing import context
from random import random
from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from Usuario.forms import UsuarioForm
from .models import Usuario
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import View
from Usuario.forms import LoginForm, UsuarioForm
from Usuario.models import Usuario


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['senha']
        print(username, password)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is None:
            print("user none")
            context = {"error": "Email ou senha inválido."}
            return render(request, "usuario/login.html", context)
        login(request, user)
        print(user)
        return redirect('/financa')
    return render(request, "usuario/login.html", context={'form': form})

def cadastro_form(request):
    context ={}
    context['form']= UsuarioForm()
    form = UsuarioForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso')
            return redirect('login')
    return render(request, "usuario/cadastro_form.html", context)

def index(request):
    try:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return redirect('login')
    except:
        messages.error(request, 'Ops, Tivemos um pequeno problema inesperado. Recarregue a página e logue novamente')
        return redirect('login')

    
def deletarUsuario(request, id):
    context ={}
    context['form']= UsuarioForm()
    form = UsuarioForm()
    print('ok')
    if request.method == "GET":
        form = Usuario.objects.get(id=id)
        form.delete()
        return redirect(request, login)

def login_page(request):
    if request.method == "POST":
        form = LoginForm()
        if form.is_valid():
            username = form.cleaned_data['email'],
            password = form.cleaned_data['senha'],
            user = authenticate(username=username, password=password)                
            print(user)
            if user is not None:
                login(request, user)
                messages.info(request, f"O {username} está logado.")
                return redirect("test")
            else:
                messages.error(request, "Email ou senha inválidos.")
        else:
            messages.error(request, "Email ou senha inválidos.")
    form = LoginForm()
    return render(request=request, template_name="usuario/login.html", context={'form':form})

