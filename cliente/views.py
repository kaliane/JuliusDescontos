from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def index (request):
	return render(request, 'index.html')

def login (request):
    return render(request, 'login.html')

def cadastro (request):
    return render(request, 'cadastro.html')

