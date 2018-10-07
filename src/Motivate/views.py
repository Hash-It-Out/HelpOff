from django.shortcuts import render

# Create your views here.
def chat(request):

	return render(request,"Motivate/chat.html",{})

def fun(request):

	return render(request,"Motivate/fun.html",{})

def motivate(request):

	return render(request,"Motivate/motivate.html",{})

def contactUs(request):
	return 
