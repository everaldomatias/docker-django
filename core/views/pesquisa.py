from django.shortcuts import render
from ..helpers import cnpj as cn
from core.models import Fundo

def pesquisa(request):
    cnpj = request.POST.get('cnpj') if request.POST.get('cnpj') else ''
    cnpj_format = ''
    if (cnpj.replace('/','').replace('-','').replace('.','') != ''):
        cnpj_format = cn.Cnpj().format(cnpj.replace('/','').replace('-','').replace('.',''))
    fundo = Fundo.objects.filter(cnpj=cnpj_format)
    if (fundo.count() > 0):
        resgate = fundo[0].resgate if hasattr(fundo[0],'resgate') else ''
        cnpj = fundo[0].cnpj if hasattr(fundo[0],'cnpj') else ''
        context = {
            'resgate': resgate,
            'cnpj': cnpj
        }
        return render(request, 'pesquisa.html', context)
    resgate = 'não existe no banco' if cnpj_format != '' else ''
    context = {
        'cnpj': cnpj_format,
        'resgate': resgate
    }
    return render(request, 'pesquisa.html', context)
