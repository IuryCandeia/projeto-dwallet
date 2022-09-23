from statistics import mode
from django.db import models
from django.contrib.auth.models import User



class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Financa(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=40)
    tipo = models.CharField(verbose_name="Tipo", max_length=20, default="Mensal")
    descricao = models.TextField(verbose_name="Descrição", max_length=250)
    valor = models.FloatField(verbose_name="Valor", max_length=20, default="0,0")

    def __str__(self):
        return "{} - {} - {} ({})".format(self.titulo, self.tipo, self.descricao, self.valor)
    