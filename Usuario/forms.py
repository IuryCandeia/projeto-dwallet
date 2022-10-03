from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from requests import post

from Usuario.models import Cliente, Usuario

GENERO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('o', 'Outros')
)

class CadastroForm(UserCreationForm):

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
    password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={"name":"senha",
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
            attrs={"name":"senha",
                "placeholder": "Confirme Senha",
                "class": "form-control",
                "data-toggle": "password",
                "id": "password",
            }
        ),
    )

    def desativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = False
        usuario.save()
        
    def ativar(request, id):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.ativo = True
        usuario.save()



class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']




class UserForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"