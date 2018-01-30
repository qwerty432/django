from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('<html><body>Hello, World!</body></html>')


def about(request):
    return HttpResponse("Here is the About Page. Want to return home? <a href='/'>Back Home</a>")


def weather(request):
    html = "Current weather in Kyiv is: 2°C. Mostly cloudly.<br><a href='/'>Back Home</a>" 
    return HttpResponse(html)