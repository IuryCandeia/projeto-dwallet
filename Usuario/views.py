import email
from multiprocessing import context
from random import random
from django.contrib import messages
from xml.dom.minidom import CharacterData
from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import View
from Usuario.forms import UsuarioForm
from Usuario.models import Usuario

class LoginView(TemplateView):
    template_name = 'login.html'

def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("senha")
        print(username, password)

        user = authenticate(request, username="email", password="password")
        print(user)
        if user is None:
            print("user none")
            context = {"error": "Email ou senha inválido."}
            return render(request, "usuario/login.html", context)
        login(request, user)
        print(user)
        return redirect('/financa')
    return render(request, "usuario/login.html", {})

def cadastro_form(request):
    context ={}
    context['form']= UsuarioForm()
    form = UsuarioForm(request.POST or None)
    print('ok')

    if Usuario.objects.filter(email='email').exists():
            messages.error(request, 'Usuário já cadastrado ')
            return redirect("login")
    if Usuario.objects.filter(username = 'username').exists():
        messages.error(request, "This username is already taken")
        return redirect('login')
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print('ok')
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
        messages.error(request, 'Ops, Tivemos um pequeno problema inesperado.Recarregue a página e logue novamente')
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