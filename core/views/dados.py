from django.views.generic import CreateView
from django.contrib import messages
from core.forms import DadosModelForm
from core.models import Dados
from django.urls import reverse_lazy


class DadosView(CreateView):
    template_name = 'dados.html'
    model = Dados
    form_class = DadosModelForm
    success_url = reverse_lazy('dados')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Dados cadastrados com sucesso')
        return super(DadosView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao cadastrar os dados')
        return super(DadosView, self).form_invalid(form, *args, **kwargs)

