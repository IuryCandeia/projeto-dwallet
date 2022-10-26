from audioop import reverse
from multiprocessing import context
from random import random
from django import forms
from django.contrib import messages, auth
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from Usuario.forms import LoginForm, UsuarioForm
from .models import Usuario
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import View
from Usuario.forms import UsuarioForm
from Usuario.models import Usuario


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(email, password)
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
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
            messages.success(request, 'Usuario cadastrado com sucesso')
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
            password = form.cleaned_data['password'],
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

def login_test(request):
    usuario = None
    message = ''
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        usuario = auth.authenticate(request, username=email, password=senha)
        print(usuario)
        if usuario != None:
            print(usuario)
            auth.login(request, usuario)
            return redirect('home')
        message = 'Login falhou!'
    return render(request, 'usuario/login.html', context={'message': message})

def login_ok(request):

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
       
        nome = Usuario.objects.filter(email=email).values_list('username', flat=True).get()
        id_usuario = Usuario.objects.filter(email=email).values_list('id', flat=True).get()
        nome_usuario_authenticated = Usuario.objects.filter(email=email).values_list('nomeUsuario', flat=True).get()
        Usuario = auth.authenticate(request, username=nome, password=senha)
        ativo_inativo = Usuario.objects.filter(email=email).values_list('ativo', flat=True).get()
        if ativo_inativo == True:
            if Usuario != None:
                auth.login(request, Usuario)

                return redirect('home')
            else:
                title_error = 'EMAIL OU SENHA INCORRETO'
                text_error = 'EMAIL OU SENHA INCORRETO'
                dados = {
                    'title_error': title_error,
                    'text_error': text_error,
                }
                return render(request, "usuario/login.html", dados)
        else:
            title_error = 'USUÁRIO DESATIVADO'
            text_error = 'USUÁRIO DESATIVADO'
            dados = {
                'title_error': title_error,
                'text_error': text_error,
            }

            return render(request, "usuario/login.html", dados)
    return render(request, "usuario/login.html")