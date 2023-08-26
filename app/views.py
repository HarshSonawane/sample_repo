from django.shortcuts import render
# import HttpResponse from django.http module
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")