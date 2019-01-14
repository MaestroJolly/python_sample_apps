from django.shortcuts import render
import json
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic.base import TemplateView
from python_rave import Rave, RaveExceptions, Misc
from django.shortcuts import render
import requests

# Create your views here.

rave = Rave("FLWPUBK-f54d8d24292e377a71620bd82a8bb17c-X",
                "FLWSECK-a18ca169cb007a93db4479aff683a387-X", usingEnv=False)


def subscriptions_view(request):
    resp1 = list_all()
    resp2 = fetch_one()

    result = {
        'list_all': resp1,
        'fetch_one': resp2
    }

    context = {'subscriptions': result}
    # returns the index.html template
    return render(request, 'subscriptions/index.html', context) 

def list_all():
    try:
        res2 = rave.Subscriptions.allSubscriptions()
    except RaveExceptions.PlanStatusError as e:
        print(e.err["errMsg"])
        print(e.err["flwRef"])
    return res2
        
      
def fetch_one():   
    try: 
        res2 = rave.Subscriptions.fetchSubscription(1180)
    except RaveExceptions.PlanStatusError as e:
        print(e.err["errMsg"])
        print(e.err["flwRef"])
    return res2
