# import requests
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def transfer(request):
    return render(request, 'transfer/index.html', context=None)