from multiprocessing import context
from random import random
from django.contrib import messages
from xml.dom.minidom import CharacterData
from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from Usuario.forms import CadastroForm, UserForm
from .models import Usuario, Financa
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import View





class LoginView(TemplateView):
    template_name = 'login.html'


def cadastro(request):
    template_name = 'cadastro_form.html'

    form = CadastroForm(request.POST or None)
    print(form.is_valid)
    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, template_name, {'form': form})

def login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        email = request.POST['email']
        senha= request.POST['senha']
        user = authenticate(request, email=email)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('usuario:inicio.html')
        else:
            print('deu caca')

    return render(request, template_name, {})


def cadastroForm(request):
    if request.method == "GET":
        print('aqui')
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'user_profile.html', context=context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            print('post')
            cliente = form.save()
            form = UserForm()

        context = {
        'form': form
    }
    return render(request, 'user_profile.html', context=context)
