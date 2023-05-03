from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
   return HttpResponse("Hello World!")

def greetings_name(request, name):
    return HttpResponse(f'Hello World, {name.capitalize()}!')


def about(request):
    c = {"title": "About me"}
    return render(
        request=request,
        template_name="infos/about.html",
        context=c
    )

def contact(request):
    c = {"title": "Contact"}
    return render(
        request=request,
        template_name="infos/contact.html",
        context=c
    )
