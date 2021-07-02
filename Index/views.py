from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import django.contrib.staticfiles
import requests
def index(request):
	return render(request,'index.html');

def post(request):
    str = request.GET.get('q')
    list = getDomains(str)
    return render(request,'result.html',{'list':list}) 

def getDomains(str):
	data = requests.get("https://park.io/domains/index/all.json?limit=100000")
	data = data.json()
	data = data['domains']
	list=[]
	for i in data:
		if(like(str,i['name'])):
			list.append(i['name'])
	return list

def like(term,domain):
	list = term.split()
	for item in list:
		if(item in domain):
			return True
	return False