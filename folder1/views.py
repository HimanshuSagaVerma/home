from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
	return HttpResponse('Hello Verma\nWelcome to Home Page')

def index1(request, number):
	return HttpResponse('Page number is %s' % number)

def first_api(request):
	my_response = {
	'contacts': [
	{
	'id': 'c200',
	'name': 'Ravi Tamada',
	'email': 'ravi@gmail.com',
	'address': 'xx-xx-xxxx,x - street, x - country',
	'gender': 'male',
	},
	{
	'id': 'c201',
	'name': 'Johnny Depp',
	'email': 'johnny_depp@gmail.com',
	'address': 'xx-xx-xxxx,x - street, x - country',
	'gender': 'male',
	},
	{
	'id': 'c202',
	'name': 'Leonardo Dicaprio',
	'email': 'leonardo_dicaprio@gmail.com',
	'address': 'xx-xx-xxxx,x - street, x - country',
	'gender': 'male',
	}
	]
	}
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)