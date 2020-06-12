from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi! Welcome to the innovation with Bootcamp training.")

def index1(request):
    return render(request, "Bootapp/home.html")

def index2(request):
    return render(request, "Bootapp/random.html")



