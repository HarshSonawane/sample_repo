from django.shortcuts import render
# import HttpResponse from django.http module
from django.http import HttpResponse

def index(request):
    q = request.GET.get('q')
    return HttpResponse("Hello World! " + q)