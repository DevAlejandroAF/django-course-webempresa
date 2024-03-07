from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h2>Inicio</h2>")


def about(request):
    return HttpResponse("<h2>Acerca de</h2>")


def services(request):
    return HttpResponse("<h2>Servicios</h2>")


def store(request):
    return HttpResponse("<h2>Tienda</h2>")


def contact(request):
    return HttpResponse("<h2>Contacto</h2>")


def blog(request):
    return HttpResponse("<h2>Blog</h2>")


def sample(request):
    return HttpResponse("<h2>Ejemplo</h2>")
