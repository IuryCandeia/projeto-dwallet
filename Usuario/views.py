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

def user_form(request):
    context ={}
    context['form']= UsuarioForm()
    form = UsuarioForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print('formulário salvo')
    return render(request, "user_form.html", context)

