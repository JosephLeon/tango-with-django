from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    about_text = {'shorttext': "Rango says here is the about page."}
    return render(request, 'rango/about.html', about_text)
