from email.policy import default
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  

class Base(models.Model):
    criado = models.DateTimeField(
        'Data de Criação', auto_now_add=True, null=True, blank=True)
    modificado = models.DateTimeField(
        'Data de Atualização', auto_now=True, null=True, blank=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Users(User, Base):
    User.username = models.CharField('Nome', max_length=100, default='')
    User.email = models.EmailField("Email", default='eu@eu.com')
    
    USERNAME_FIELD = 'email'
    
    def statusAtivo(self):
        if self.ativo == True:
            return "Ativo"
        else:
            return "Inativo"
