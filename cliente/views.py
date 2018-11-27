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

<<<<<<< HEAD
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
<<<<<<< HEAD
        form = SignUpForm()
    return render(request, '../templates/cadastro.html', {'form': form})
=======
        form = formCadastro()
    return render(request, 'cadastro.html', {'form': form})
=======
def cadastroPromocao (request):
	return render(request, 'cadastroPromocao.html')	
>>>>>>> f1a28a4a2b50231f1204ba94c795e30b13bb638a

>>>>>>> 5cdc24949c22d6bdc9d8dc9d1e24680396956cfb
