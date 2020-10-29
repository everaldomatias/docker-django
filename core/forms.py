from django import forms
from .models import Dados, Index


class IndexModelForm(forms.ModelForm):
    data = forms.DateField(input_formats=['%YYYY/%mm/%dd'])

    class Meta:
        model = Index
        fields = ['cnpj', 'data']


class DadosModelForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['cnpj', 'denom_social', 'data', 'vltotal', 'vlquota',
                  'vlpatrimliq', 'captcdia', 'resgdia', 'nrcotst']

