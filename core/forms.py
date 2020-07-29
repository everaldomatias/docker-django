from django import forms
from .models import Dados


class DadosModelForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['cnpj', 'data', 'vltotal', 'vlquota',
                  'vlpatrimliq', 'captcdia', 'resgdia', 'nrcotst']