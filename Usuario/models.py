from email.policy import default
from statistics import mode
from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField
from pkg_resources import require


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
    User.nome = models.CharField('Nome', max_length=100, unique=True, default='')
    User.email = models.EmailField("Email", default='eu@eu.com')
    telefone = models.CharField("Telefone", max_length=21, default='(83)99999-9999', blank=True, null=True)
    
    
    def statusAtivo(self):
        if self.ativo == True:
            return "Ativo"
        else:
            return "Inativo"

"""Multipla escolha para genero sexual"""
GENERO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('o', 'Outros')
)
class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=50)
    data_nascimento = models.DateField("Data de Nascimento", blank=True, null=True)
    genero = models.CharField("Gênero", max_length=1, choices= GENERO_CHOICES)
    email = models.EmailField("Email", max_length=50)

    def __str__(self):
        return self.nome

class Financa(models.Model):
    titulo = models.CharField("Título", max_length=40)
    tipo = models.CharField("Tipo", max_length=20, default="Mensal")
    descricao = models.TextField("Descrição", max_length=250)
    valor = models.FloatField("Valor", max_length=20, default="0,0")

    def __str__(self):
        return "{} - {} - {} ({})".format(self.titulo, self.tipo, self.descricao, self.valor)


