from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from cliente.forms import formCadastro

def index (request):
	return render(request, 'index.html')

def loogin (request):
    return render(request, 'login.html')

def cadastro (request):
    return render(request, 'cadastro.html')

def recSenha (request):
    return render(request, 'recSenha.html')

def cadastroSuc (request):
    return render(request, 'cadastroSuc.html')

def cadastro(request):
    print(request.method)
    if request.method == 'POST':
        form = formCadastro(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password1')
            user = authenticate(username=usuario, password=senha)
            login(request, user)
            return HttpResponseRedirect('loogin')
    else:
        form = formCadastro()
    return render(request, 'cadastro.html', {'form': form})

