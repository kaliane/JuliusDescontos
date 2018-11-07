from django.urls import path
from.views import index
from.views import login
from.views import cadastro
from.views import recSenha

urlpatterns = [
	path('index', index),
    path('login', login),
    path('cadastro', cadastro),
    path('recSenha', recSenha),
]