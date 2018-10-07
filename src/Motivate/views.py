from django.shortcuts import render
from .tone import ToneAnalyze
from bs4 import BeautifulSoup
import requests
import json

# Create your views here.
from pprint import pprint

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

def contact_us(request):
	consultant=[
		{
			"name":"Devansh",
			"email":"devanshslnk98@gmail.com",
			"contact":999,
			"speciality":"Fear"
		},
		{
			"name":"consultant2",
			"email":"priyamshah112@gmail.com",
			"contact":991,
			"speciality":"Anger"
		},
		{
			"name":"consultant3",
			"email":"priyams972@gmail.com",
			"contact":990,
			"speciality":"Sadness"

		}
	]
	if(request.method=="POST"):
		first_name=request.POST.get("firt_name")
		last_name=request.POST.get("last_name")
		email=request.POST.get("mail")
		subject=request.POST.get("subject")
		message=request.POST.get("message")
		result=ToneAnalyze.analyze(message)
		average_tones=result['document_tone']['tones']
		
		maximum=0
		print(average_tones)
		final_tone={}
		for i in average_tones:
			if(i['score']>maximum and (i['tone_name']=='Sadness' or i['tone_name']=='Anger' or i['tone_name']=='Fear')):
				final_tone=i
		if(final_tone['tone_name']=="Sadness"):
			return render(request,"Motivate/consultant.html",consultant[2])
		elif(final_tone['tone_name']=="Fear"):
			return render(request,"Motivate/consultant.html",consultant[0])
		else:
			return render(request,"Motivate/consultant.html",consultant[1])
		



