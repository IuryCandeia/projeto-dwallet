from email.policy import default
from statistics import mode
from django.contrib.auth.models import User
from django.db import models

class Usuario(User):
    User.username = models.CharField(
        'Nome', max_length=100, unique=True, default='')
    telefone = models.CharField(
        "Telefone", max_length=21, default='(83)99999-9999', blank=True, null=True)
    User.email = models.EmailField("Email", default='eu@eu.com')
    
    def statusAtivo(self):
        if self.ativo == True:
            return "Ativo"
        else:
            return "Inativo"
   


class Financa(models.Model):
    titulo = models.CharField("Título", max_length=40)
    tipo = models.CharField("Tipo", max_length=20, default="Mensal")
    descricao = models.TextField("Descrição", max_length=250)
    valor = models.FloatField("Valor", max_length=20, default="0,0")

    def __str__(self):
        return "{} - {} - {} ({})".format(self.titulo, self.tipo, self.descricao, self.valor)