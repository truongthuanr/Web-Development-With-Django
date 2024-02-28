from django.shortcuts import render
from django.http import HttpResponse
from bookr import settings

# Create your views here.
def spending(request):
    if settings.DEBUG: print("Run spending()")
    
    return "ABCXYZ"
