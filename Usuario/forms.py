from unicodedata import name
from attr import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  AuthenticationForm
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from requests import post
from Usuario.models import Usuario
from Usuario.validacao import comparando_senhas, duplicidade_email,  duplicidade_id


class UsuarioForm(forms.Form):
    username = forms.CharField(label= 'Nome', required=True ,widget= forms.TextInput(
        attrs={'name': 'nome','placeholder': 'Nome', 'class': 'form-control'}))
    sobrenome = forms.CharField(label='Sobrenome' , max_length=100, required=False, widget= forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, max_length=150, widget= forms.TextInput(
        attrs={'name': 'email','placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget= forms.PasswordInput(
        attrs={'name': 'senha','placeholder': 'Senha', 'class': 'form-control'}), required=True, min_length=8)
    password1 = forms.CharField(label='Confirmação de senha', widget= forms.PasswordInput(
        attrs={'name': 'conf_senha', 'placeholder': 'Confirmar Senha', 'class': 'form-control'}), required=True, min_length=8)


    def save(self):
        data = self.cleaned_data
        comparando_senhas(data['password'], data['password1'])
        duplicacao_email = duplicidade_email(data['email'])
        id_duplicado = duplicidade_id(data['username'])

        if duplicacao_email == False and id_duplicado == False:
            user = Usuario(username=data['username'], email=data['email'], 
                            password=data['password'])
            user.save()
            return [duplicacao_email, id_duplicado, user.id]
        else:
            return [duplicacao_email, id_duplicado]
    
   
    def desativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = False
        usuario.save()
        
    def ativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = True
        usuario.save()

    class Meta:
        model = User
        fields = ('username', 'sobrenome', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"name": "username",
                "placeholder" : "Digite seu nome de usuário",
                "class": "form-control",
            }
        ))
    senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"name": "password",
                "placeholder" : "Digite sua Senha",
                "class": "form-control",
            }
        ))
 

