from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	return render(request, 'index.html')
	#return HttpResponse('This is Homepage')

def about(request):
	return HttpResponse('This is about page')

def contact(request):
	return HttpResponse("This is Contact Us Page")