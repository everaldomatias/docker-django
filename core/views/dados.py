from django.shortcuts import render
from django.contrib import messages
from .forms import DadosModelForm


def dados(request):
    if str(request.method) == 'POST':
        form = DadosModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'Dados cadastrados com sucesso')
            form = DadosModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar os dados.')
    else:
        form = DadosModelForm()
    context = {
        'form': form
    }

    return render(request, 'dados.html', context)