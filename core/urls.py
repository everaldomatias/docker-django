from django.urls import path
from .views import DadosJSONView
from .views import index, contato, pesquisa, DadosView

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato),
    path('pesquisa/', pesquisa),
    path('dados/', DadosView.as_view(), name='dados'),
    path('dados_grafico/', DadosJSONView.as_view(), name='dados_grafico'),
]

