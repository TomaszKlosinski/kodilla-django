from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
   return HttpResponse("Hello World!")

def greetings_name(request, name):
    return HttpResponse(f'Hello World, {name.capitalize()}!')
