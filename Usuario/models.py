from email.policy import default
from statistics import mode
from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    User.nome = models.CharField(max_length=150, default='')
    numero = models.CharField(max_length=15, default='')
    User.email = models.CharField(max_length=50, default='')
    
    def __str__(self):
        return self.nome


class Financa(models.Model):
    titulo = models.CharField("Título", max_length=40)
    tipo = models.CharField("Tipo", max_length=20, default="Mensal")
    descricao = models.TextField("Descrição", max_length=250)
    valor = models.FloatField("Valor", max_length=20, default="0,0")

    def __str__(self):
        return "{} - {} - {} ({})".format(self.titulo, self.tipo, self.descricao, self.valor)