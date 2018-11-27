from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from cliente.forms import SignUpForm


def index (request):
	return render(request, '../templates/index.html')

def deslogar (request):
    return render(request, '../templates/deslogado.html')

def loogin (request):
    return render(request, '../templates/login.html')

def cadastro (request):
    return render(request, '../templates/cadastro.html')

def recSenha (request):
    return render(request, '../templates/recSenha.html')

def cadastroSuc (request):
    return render(request, '../templates/cadastroSuc.html')

def cadastro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('loogin')
    else:
        form = SignUpForm()
    return render(request, '../templates/cadastro.html', {'form': form})