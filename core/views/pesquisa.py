from django.shortcuts import render
from ..helpers import cnpj as cn
from core.models import Fundo

def pesquisa(request):
    cnpj = request.POST.get('current_string') if request.POST.get('current_string') else ''
    cnpj_format = cn.Cnpj().format(cnpj.replace('/','').replace('-','').replace('.',''))
    print(cnpj_format)
    fundo = Fundo.objects.filter(cnpj=cnpj_format)
    resgate = fundo[0].resgate if hasattr(fundo[0],'resgate') else ''
    cnpj = fundo[0].cnpj if hasattr(fundo[0],'cnpj') else ''
    context = {
        'resgate': resgate,
        'cnpj': cnpj
    }
    return render(request, 'pesquisa.html', context)