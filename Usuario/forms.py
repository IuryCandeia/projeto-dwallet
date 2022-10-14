from unicodedata import name
from attr import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from requests import post

from Usuario.models import Usuario
from Usuario.validacao import comparando_senhas,  duplicidade_id

GENERO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('o', 'Outros')
)


class UsuarioForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"name":"nome",
                "placeholder": "Nome",
                "class": "form-control",
                "id": 'username',
            }
        ),
    )
    telefone = forms.CharField(
        label="Número Telefone",
        widget=forms.TextInput(
            attrs={"name":"telefone",
                "placeholder": "Número telefone",
                "id": "id_telefone",
                "class": "form-control",
            }
        ),
    )
    genero = forms.ChoiceField(choices=GENERO_CHOICES)
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={"name":"Email",
                "placeholder": "Email",
                "class": "form-control",
            }
        ),
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def desativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = False
        usuario.save()
        
    def ativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = True
        usuario.save()



class UsuarioForm(forms.Form):
    username = forms.CharField(label= 'Nome', required=True ,widget= forms.TextInput(
        attrs={'name': 'nome','placeholder': 'Nome', 'class': 'form-control'}))
    sobrenome = forms.CharField(label='Sobrenome' , max_length=100, required=False, widget= forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, max_length=150, widget= forms.TextInput(
        attrs={'name': 'email','placeholder': 'Email', 'class': 'form-control'}))
    genero = forms.ChoiceField(label='Gênero' , choices=GENERO_CHOICES)
    telefone = forms.CharField(label='Número de telefone', required=True, max_length=13, widget= forms.NumberInput(
        attrs={'placeholder': 'Telefone', 'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget= forms.PasswordInput(
        attrs={'name': 'senha','placeholder': 'Senha', 'class': 'form-control'}), required=True, min_length=8)
    password1 = forms.CharField(label='Confirmação de senha', widget= forms.PasswordInput(
        attrs={'name': 'conf_senha', 'placeholder': 'Confirmar Senha', 'class': 'form-control'}), required=True, min_length=8)

    def save(self):
        data = self.cleaned_data
        comparando_senhas(data['password'], data['password1'])
        user = Usuario(username=data['username'], email=data['email'], telefone=data['telefone'], 
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

    class Meta:
        model = User
        fields = ('username', 'sobrenome', 'email', 'genero', 'telefone', 'password1', 'password2')

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={"name": "email",
                "placeholder" : "Digite seu Email",
                "class": "form-control",
            }
        ))
    senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"name": "senha",
                "placeholder" : "Digite sua Senha",
                "class": "form-control",
            }
        ))


