from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home</h1>')

def form(request):
    return HttpResponse('<h1>Form</h1>')