import email
from django.db import models
from django.contrib.auth.models import User



class Usuario(User):
    User.nome = models.CharField('nome',max_length=100, unique=True, default='')
    User.email = models.EmailField("Email", default='eu@eu.com')
    telefone = models.CharField("Telefone", max_length=21, default='(83)99999-9999', blank=True, null=True)
    senha = models.CharField("senha", max_length=50)

    def __str__(self):
        return self.nome