from django.shortcuts import render
from .tone import ToneAnalyze
from bs4 import BeautifulSoup
import requests
import json

# Create your views here.
from pprint import pprint
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
		



