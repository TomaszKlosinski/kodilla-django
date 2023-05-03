from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    c = {"title": "Homepage"}
    return render(
        request=request,
        template_name="infos/home.html",
        context=c
    )

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
