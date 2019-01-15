from django.shortcuts import render
import json
import os
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic.base import TemplateView
from python_rave import Rave, RaveExceptions, Misc
from django.shortcuts import render
import requests
import webbrowser

# Create your views here.
RAVE_PUBLIC_KEY = os.getenv('RAVE_PUBLIC_KEY')
RAVE_SECRET_KEY = os.getenv('RAVE_SECRET_KEY')
rave = Rave(RAVE_PUBLIC_KEY, RAVE_SECRET_KEY, usingEnv=True)


@require_http_methods(["GET", "POST"])
@csrf_exempt

# view to render tokenized index page
def tokenized(request):
    return render(request, 'tokenized/index.html', context=None)

# view for card charge
def card_charge(request):
    if request.POST and request.is_ajax():
        cardNo = request.POST.get('cardNo')
        exMonth = request.POST.get('exMonth')
        exYear = request.POST.get('exYear')
        cvv = request.POST.get('cvv')
        pin = request.POST.get('pin')
        cardAmount = request.POST.get('cardAmount')

        payload = {
            "cardno": cardNo,
            "cvv": cvv,
            "expirymonth": exMonth,
            "expiryyear": exYear,
            "amount": cardAmount,
            "email": "user@gmail.com",
            "phonenumber": "0902620185",
            "firstname": "temi",
            "lastname": "desola",
            "IP": "355426087298442",
            "redirect_url": "http://127.0.0.1:8000/tokenized/redirect_url/"
        }
        try:
            res = rave.Card.charge(payload)
            print(res)
            if res["suggestedAuth"]:
                arg = Misc.getTypeOfArgsRequired(res["suggestedAuth"])

                if arg == "pin":
                    Misc.updatePayload(res["suggestedAuth"], payload, pin=pin)
                if arg == "address":
                    Misc.updatePayload(res["suggestedAuth"], payload, address={"billingzip": "07205", "billingcity": "Hillside", "billingaddress": "470 Mundet PI", "billingstate": "NJ", "billingcountry": "US"})

                res = rave.Card.charge(payload)
                print(res)

                if res["validationRequired"]:
                    rave.Card.validate(res["flwRef"], "12345")
                    res = rave.Card.verify(res["txRef"])
                    print(res["transactionComplete"])
            else:
                auth_url = res["authUrl"]
                webbrowser.open(auth_url)

        except RaveExceptions.CardChargeError as e:
            print(e.err["errMsg"])
            print(e.err["flwRef"])

        except RaveExceptions.TransactionValidationError as e:
            print(e.err)
            print(e.err["flwRef"])

        except RaveExceptions.TransactionVerificationError as e:
            print(e.err["errMsg"])
            print(e.err["txRef"])

        data = res
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404

# view for tokenized charge

def token_charge(request):
    if request.POST and request.is_ajax():
        inputToken = request.POST.get('inputToken')
        tokenAmount = request.POST.get('tokenAmount')

        payload_for_saved_card = {
            "token": inputToken,
            "amount": tokenAmount,
            "email": "user@gmail.com",
            "currency": "NGN",
            "country": "NG",
            "phonenumber": "0902620185",
            "firstname": "temi",
            "lastname": "desola",
            "IP": "355426087298442",
        }

        try:
            res = rave.Card.charge(payload_for_saved_card, chargeWithToken=True)
            print(res)
            res = rave.Card.verify(res["txRef"])
            print(res)
            print(res["transactionComplete"])
            data = res

        except RaveExceptions.CardChargeError as e:
            print(e.err["errMsg"])
            print(e.err["flwRef"])
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404

# view for redirect url
    
def redirect_url(request):
    request_json = request.GET["response"]
    print(request_json)
    return HttpResponse(request_json)

