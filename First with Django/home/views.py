from django.shortcuts import render, HttpResponse
from django.urls.conf import path
from django import urls


# Create your views here.

def index(request):
	context = {
		"variable1" : "Var1",
		"title" : "Home"
	}
	return render(request, 'index.html', context)
	#return HttpResponse('This is Homepage')

def about(request):
	context = {
		"variable1" : "Var1",
		"title" : "About"
	}
	return render(request, 'about.html', context)

def contact(request):
	context = {
		"variable1" : "Var1",
		"title" : "Contact"
	}
	return render(request, 'contact.html', context)