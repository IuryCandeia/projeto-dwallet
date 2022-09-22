import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import User



class Usuario(User, models.Model):
    User.nome = models.CharField('nome',max_length=100, default='')
    User.email = models.EmailField("Email", unique=True, default='eu@eu.com')
    telefone = models.CharField("telefone", max_length=21, default='(83)99999-9999', blank=True, null=True)
    senha = models.CharField("senha", max_length=50)

    def __str__(self):
        return "{} ({})".format(self.nome, self.email, self.telefone, self.senha)

class Login(models.Model):
    email = models.EmailField(("email"), max_length=254,unique=True, default="a@aa.com.br")
    senha = models.CharField(("senha"), max_length=50)

    def __str__(self):
        return "{} ({})".format(self.email, self.senha)


