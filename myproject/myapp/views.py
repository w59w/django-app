
from django.shortcuts import render
from django.http import HttpResponse


def text_response(request):
    return HttpResponse("Это текстовый ответ")


def html_response(request):
    return render(request, 'myapp/example.html')


def index(request):
    return HttpResponse("Welcome to the home page!")  # Ответ для главной страницы
