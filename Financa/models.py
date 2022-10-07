from xml.etree.ElementInclude import default_loader
from django.db import models

class Financa(models.Model):
    titulo = models.CharField("Título", max_length= 100, default="")
    descricao = models.CharField("Descrição", default="")
    valor = models.DecimalField("Valor", decimal_places=2)

    class Meta:
            abstract = True