import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import User



class Usuario(User):
    nome = models.CharField('nome',max_length=100, default='')
    User.email = models.EmailField("Email", unique=True, default='eu@eu.com')
    telefone = models.CharField("telefone", max_length=21, default='(83)99999-9999', blank=True, null=True)
    User.senha = models.CharField("senha", max_length=50)

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.email, self.telefone, self.senha)


class Financa(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=40)
    tipo = models.CharField(verbose_name="Tipo", max_length=20, default="Mensal")
    descricao = models.TextField(verbose_name="Descrição", max_length=250)
    valor = models.FloatField(verbose_name="Valor", max_length=20, default="0,0")

    def __str__(self):
        return "{} - {} - {} ({})".format(self.titulo, self.tipo, self.descricao, self.valor)
    