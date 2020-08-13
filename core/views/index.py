from django.shortcuts import render
from core.forms import IndexModelForm
from core.models import Dados


def index(request):
    cnpj = request.POST.get('cnpj') if request.POST.get('cnpj') else ''
    form = IndexModelForm(request.POST)
    if form.is_valid():
        form = IndexModelForm()

    context = {
        'itens': Dados.objects.filter(cnpj=cnpj),
        'cnpj': cnpj,
        'form': form,
    }

    return render(request, 'index.html', context)
