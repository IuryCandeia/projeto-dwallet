from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404
from requests import post

from Usuario.models import Usuario


class CadastroForm(UserCreationForm):

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "class": "form-control",
                "id": 'username',
            }
        ),
    )
    telefone = forms.CharField(
        label="Número Telefone",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Número telefone",
                "id": "id_telefone",
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
            }
        ),
    )
    password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control",
                "data-toggle": "password",
                "id": "password",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirme Senha",
                "class": "form-control",
                "data-toggle": "password",
                "id": "password",
            }
        ),
    )


    def save(self):
        data = self.cleaned_data
        user = Usuario(username=data['username'], telefone=data['telefone'], email=data['email'], password=data['senha'])
        user.save()

    def desativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = False
        usuario.save()
        
    def ativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = True
        usuario.save()
