from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(("nome"), max_length=60)
    email = models.EmailField(("email"), max_length=254,unique=True, default="a@aa.com.br")

    def __str__(self):
        return "{} ({})".format(self.nome + self.email)

class Login(models.Model):
    email = models.EmailField(("email"), max_length=254,unique=True, default="a@aa.com.br")
    senha = models.CharField(("senha"), max_length=50)