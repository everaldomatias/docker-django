from django.shortcuts import render
from core.forms import IndexModelForm
from core.models import Dados


def index(request):
    cnpj = request.POST.get('cnpj') #if request.POST.get('cnpj') else ''
    data = request.POST.get('data') #if request.POST.get('data') else ''
    form = IndexModelForm(request.POST)

    if form.is_valid():
        form = IndexModelForm()

    itens = Dados.objects.filter(cnpj=cnpj, data=data)
    for i in itens:
        i.jan = i.vltotal + i.vlpatrimliq
        i.ano = data[:4]
        form = IndexModelForm()
    context = {
        'itens': itens,
        'cnpj': cnpj,
        'form': form,
        'data': data,
    }

    return render(request, 'index.html', context)
