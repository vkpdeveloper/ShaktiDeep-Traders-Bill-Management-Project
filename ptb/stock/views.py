from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Helllo World Welcome to stock')
