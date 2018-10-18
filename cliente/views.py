from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def login (request):
	return render(request, 'login.html')

