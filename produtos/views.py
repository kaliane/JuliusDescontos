from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def cadastroPromocao (request):
	return render(request, '../templates/cadastroPromocao.html')



