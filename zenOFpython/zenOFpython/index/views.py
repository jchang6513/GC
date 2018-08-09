from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.http import HttpResponse
from .zens import randzen
import os

def index(request):
	return render(request, 'index.html', {'zen':randzen()})