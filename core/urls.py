from django.urls import path
from .views import index, contato, pesquisa, dados

urlpatterns = [
    path('', index),
    path('contato/', contato),
    path('pesquisa/', pesquisa),
    path('dados/', dados, name='dados')
]
