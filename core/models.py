from django.db import models


class Index(models.Model):
    cnpj = models.CharField('CNPJ', max_length=100)
    data = models.DateField('Data', blank=True, null=True)

    def __str__(self):
        return self.cnpj


class Fundo(models.Model):
    cnpj = models.CharField(max_length=200)
    resgate = models.IntegerField()


class Arquivos(models.Model):
    nome = models.CharField(max_length=200)
    tamanho = models.IntegerField()


class Dados(models.Model):
    cnpj = models.CharField('CNPJ', max_length=100)
    denom_social = models.CharField('Denominação Social', max_length=300, blank=True, null=True)
    data = models.DateField('Data', blank=True, null=True)
    vltotal = models.DecimalField('Valor Total', max_digits=20, decimal_places=2)
    vlquota = models.DecimalField('Valor Quota', max_digits=15, decimal_places=7, blank=True, null=True)
    vlpatrimliq = models.DecimalField('Valor Pat Liq', max_digits=20, decimal_places=2)
    captcdia = models.DecimalField('Captc Dia', max_digits=20, decimal_places=2)
    resgdia = models.DecimalField('Resgate Dia', max_digits=20, decimal_places=2)
    nrcotst = models.IntegerField('Nr Cotst', blank=True, null=True)

    def __str__(self):
        return self.cnpj


