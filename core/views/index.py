from django.shortcuts import render
from core.forms import IndexModelForm
from core.models import Dados
from random import randint
from chartjs.views.lines import BaseLineChartView


def index(request):
    IndexModelForm(request.POST)
    cnpj = request.POST.get('cnpj')
    data = request.POST.get('data')
    form = IndexModelForm()
    if form.is_valid():
        IndexModelForm()
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


class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        '''Retorna  12 labels para a representação do x'''
        labels = [
            'Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro'
        ]

        return labels

    def get_providers(self):
        'Retorna os nomes dos datasets'
        datasets = [
            'Valor Total',
            'Valor da Cota',
            'Patrimonio Liquido',
            'Capatc Dia',
            'Resgate Dia',
            'Números de cotistas'
        ]

        return datasets

    def get_data(self):
        '''
        Retorna 6 datasets para plotar o gráfico

        Cada linha representa um dataset
        Cada coluna representa um label

        A quantidade de dados precisa ser igual aos datasets/labels
        12 labels, 12 colunas
        6 datasets, 6 linhas
        '''
        dados = []
        for l in range(6):
            for c in range(12):
                dado = [
                    randint(1, 200),  # jan
                    randint(1, 200),  # fev
                    randint(1, 200),  # mar
                    randint(1, 200),  # abr
                    randint(1, 200),  # mai
                    randint(1, 200),  # jun
                    randint(1, 200),  # jul
                    randint(1, 200),  # ago
                    randint(1, 200),  # set
                    randint(1, 200),  # out
                    randint(1, 200),  # nov
                    randint(1, 200),  # dez
                ]
            dados.append(dado)
        return dados