from unittest.util import _MAX_LENGTH
from xml.etree.ElementInclude import default_loader
from django.db import models

class Financa(models.Model):
    titulo = models.CharField("Título", max_length= 100, default="")
    descricao = models.CharField("Descrição", default="", max_length= 1024)
    valor = models.DecimalField("Valor", decimal_places=2, max_digits= 12)

    def __str__(self) :
        return self.titulo