from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "rubble/index.html")


def andrew(request):
    return HttpResponse("Hello, Andrew!")


def greet(request, name):
    return render(request, "rubble/greet.html", {
        "name" : name.capitalize()
    })
    