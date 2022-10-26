import email
from email.policy import default
from statistics import mode
from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField
from pkg_resources import require

GENERO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('o', 'Outros')
)

class Base(models.Model):
    criado = models.DateTimeField(
        'Data de Criação', auto_now_add=True, null=True, blank=True)
    modificado = models.DateTimeField(
        'Data de Atualização', auto_now=True, null=True, blank=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

"""Modelo de Usúario"""
class Usuario(User, Base):
    User.username = models.CharField('Nome', max_length=100, default='')
    sobrenome = models.CharField("Nome", max_length=150, default='')
    User.email = models.EmailField("Email", default='eu@eu.com')
    
    USERNAME_FIELD = 'email'
    
    def statusAtivo(self):
        if self.ativo == True:
            return "Ativo"
        else:
            return "Inativo"






