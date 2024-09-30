from django.shortcuts import render
from django.http import HttpResponse

def get_places(request):
    return HttpResponse('Hello World!')