from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	context = {
		"variable1" : "Var1",
		"title" : "Home"
	}
	return render(request, 'index.html', context)
	#return HttpResponse('This is Homepage')

def about(request):
	return HttpResponse('This is about page')

def contact(request):
	return HttpResponse("This is Contact Us Page")