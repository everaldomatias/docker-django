from django.shortcuts import render

def index(request):
    context = {
        'descricao': 'Sistema de consulta de dados',
        'empresa': 'Pele Vermeleha',
    }
    return render(request, 'index.html', context)
