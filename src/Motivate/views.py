from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json

# Create your views here.
def chat(request):

	return render(request,"Motivate/chat.html",{})

def fun(request):
	
	joke = [None]*10
	answer = [None]*10
	for i in range(0,10):
		link = "https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke"
		source_code = requests.get(link)
		plain_text = source_code.text
		a = json.loads(plain_text)
		joke[i] = a['setup']
		answer[i] = a['punchline']
		
		context = {
			'joke':joke,
			'answer':answer,
		}


	return render(request,"Motivate/fun.html",context)

def motivate(request):

	return render(request,"Motivate/Motivate.html",{})

def motivatequote(request):
	link = "http://inspirobot.me/api?generate=true"
	source_code = requests.get(link)
	plain_text = source_code.text
	context = {
    	'img':plain_text,
    }

	return render(request,"Motivate/motivationalquotes.html",context)

def motivatevideo(request):

	return render(request,"Motivate/motivational-videos.html",{})


def motivatestories(request):

	return render(request,"Motivate/motivational-stories.html",{})
