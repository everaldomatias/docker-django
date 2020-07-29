from django.urls import path
from .views import index, contato, pesquisa, dados

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('pesquisa/', pesquisa, name='pesquisa'),
    path('dados/', dados, name='dados'),
]
