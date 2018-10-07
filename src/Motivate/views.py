from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json

# Create your views here.
def chat(request):

	return render(request,"Motivate/chat.html",{})

def fun(request):
	link = "https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke"
	source_code = requests.get(link)
	plain_text = source_code.text
	a = json.loads(plain_text)
	print(a['setup']+ "\n"+a['punchline'])
	context = {
    	'setup':a['setup'],
    	'punchline':a['punchline']
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

