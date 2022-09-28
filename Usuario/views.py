from random import random
from django.contrib import messages
from xml.dom.minidom import CharacterData
from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from Usuario.forms import CadastroForm, LoginForm
from .models import Usuario, Financa
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import View




class CadastroView(TemplateView):
    form_class = CadastroForm
    initial = {'key': 'value'}
    template_name = 'cadastro_form.html'

    def get(self, request, *args, **kwargs):
        print('ok')
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print('post cadstro')
        if form.is_valid():
            form.save()
            print('ok')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}')
            print('ok')
            return redirect(to='')

        return render(request, self.template_name, {'form': form})

class LoginView(TemplateView):
    template_name = 'login.html'
    initial = {'key': 'value'}
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print('ok')

        return render(request, self.template_name, {'form': form})



