from django.db import models


class Fundo(models.Model):
    cnpj = models.CharField(max_length=200)
    resgate = models.IntegerField()

class Arquivos(models.Model):
    nome = models.CharField(max_length=200)
    tamanho = models.IntegerField()
