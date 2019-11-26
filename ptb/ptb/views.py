from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'ptb/index.html')

def contact(request):
    return HttpResponse("Hello World !")