import email
from enum import Flag
from unicodedata import name
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from requests import post
from sqlalchemy import null

from Usuario.models import Usuario
from Usuario.validacao import comparando_senhas,  duplicidade_id

GENERO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('o', 'Outros')
)


class UsuarioForm(forms.Form):
    nome = forms.CharField(label= 'Nome', max_length=100, min_length=3, required=True)
    sobrenome = forms.CharField(label='Sobrenome' , max_length=100, min_length=3, required=True)
    email = forms.EmailField(label='Email', required=True, max_length=150)
    genero = forms.ChoiceField(label='Gênero' , choices=GENERO_CHOICES)
    telefone = forms.CharField(label='Número de telefone', required=True, max_length=13, min_length=11)
    password = forms.CharField(label='Senha', widget= forms.PasswordInput(), required=True, min_length=8)
    password1 = forms.CharField(label='Confirmação de senha', widget= forms.PasswordInput(), required=True, min_length=8)

    def save(self):
        data = self.cleaned_data
        comparando_senhas(data['password'], data['password1'])
        user = Usuario(username=data['nome'], email=data['email'], telefone=data['telefone'], 
                            genero=data['genero'], password=data['password'])
        user.save()
   
    def desativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = False
        usuario.save()
        
    def ativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = True
        usuario.save()

