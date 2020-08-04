from django import forms
from .models import Dados, Index


class IndexModelForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = ['cnpj', 'data']


class DadosModelForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['cnpj', 'data', 'vltotal', 'vlquota',
                  'vlpatrimliq', 'captcdia', 'resgdia', 'nrcotst']

