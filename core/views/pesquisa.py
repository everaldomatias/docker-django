from django.shortcuts import render
from ..helpers import cnpj as cn
from core.models import Dados


def pesquisa(request):
    cnpj = request.POST.get('cnpj') if request.POST.get('cnpj') else ''
    context = {
        'itens': Dados.objects.filter(cnpj=cnpj),
        'cnpj': cnpj
    }

    return render(request, 'pesquisa.html', context)



