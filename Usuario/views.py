from audioop import reverse
import email
from multiprocessing import context
from random import random
from django import forms
from django.contrib import messages
from xml.dom.minidom import CharacterData
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
<<<<<<< HEAD
from Usuario.forms import CadastroForm, UserForm, UsuarioForm
from .models import Usuario, Financa
from django.views.generic.edit import CreateView
=======
>>>>>>> 372dbfba5dfb4301407e15d98b3a5922ea4fbc0b
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import View
from Usuario.forms import LoginForm, UsuarioForm
from Usuario.models import Usuario

<<<<<<< HEAD
class UsuarioCreate(CreateView):
    template_name = 'form.html'
    form_class = UsuarioForm
    sucess_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
=======
def test(request):
    return render(request, 'usuario/test.html')

# def login_views(request):
#     if request.method == 'POST':
>>>>>>> 372dbfba5dfb4301407e15d98b3a5922ea4fbc0b

        context['titulo'] = "Cadastrar novo usuário"
        context['botao'] = "Cadastrar"

<<<<<<< HEAD
        return context 

def inicio(request):
    template_name = 'inicio.html'
    
    return render(request, template_name)
=======
#     else:
#         form = AuthenticationForm()
    # return render(request)
def login_view(request):
    
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['senha']
        print(username, password)

        user = authenticate(request, username="email", password="senha")
        print(user)
        if user is None:
            print("user none")
            context = {"error": "Email ou senha inválido."}
            return render(request, "usuario/login.html", context)
        login(request, user)
        print(user)
        return redirect('/financa')
    return render(request, "usuario/login.html", {})
>>>>>>> 372dbfba5dfb4301407e15d98b3a5922ea4fbc0b

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
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['email'],
                password = form.cleaned_data['senha'],
            )
               
            print(user)
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'usuario/login.html', context={'form': form, 'message': message})


def Register(request):
    form = UsuarioForm()

    if request.method == "POST":
        context = {'has_error': False}
        username = request.POST.get('nome')
        sobrenome = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        password1 = request.POST.get('conf_senha')


        if password != password1:
            messages.error(request, '⚠️ Password Mismatch! Your Passwords Do Not Match')
            return redirect('cadastro_form')

        if not username:
            messages.error(request, '⚠️ Username is required!')
            return redirect('cadastro_form')

        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username is taken! Choose another one')

            return render(request, "usuario/cadastro_form.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, '⚠️ Email is taken! Choose another one')

            return render(request, 'cadastro_form')

        user = User.objects.create_user(username=username, sobrenome=sobrenome, email=email)
        user.set_password(password)
        user.save()
        print('ok')
    print('out')
    return render(request,  "usuario/cadastro_form.html", {'form':form})