import requests
import os
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def transfer(request):
    RAVE_PUBLIC_KEY = os.environ['RAVE_PUBLIC_KEY']
    url = 'https://ravesandboxapi.flutterwave.com/v2/banks/NG?public_key=' + RAVE_PUBLIC_KEY
    # print (url)
    bank_lists = requests.get(url).json()
    banks = bank_lists["data"]["Banks"]
    context = {
        "banks": banks
    }
    return render(request, 'transfer/index.html', context)