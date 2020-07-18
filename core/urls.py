from django.urls import path
from .views import index, contato, pesquisa

urlpatterns = [
    path('', index),
    path('contato/', contato),
    path('pesquisa/', pesquisa),
]
