from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hi. <a href='/rango/about'>About page.</a>")


def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango'>Home page.</a>")
