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

# Create your views here.
RAVE_PUBLIC_KEY = os.getenv('RAVE_PUBLIC_KEY')
RAVE_SECRET_KEY = os.getenv('RAVE_SECRET_KEY')
rave = Rave(RAVE_PUBLIC_KEY, RAVE_SECRET_KEY, usingEnv=True)


@require_http_methods(["GET", "POST"])
@csrf_exempt
def preauth(request):
    return render(request, 'preauth/index.html', context=None)


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
        }
        try:
            res = rave.Card.charge(payload)
            if res["suggestedAuth"]:
                arg = Misc.getTypeOfArgsRequired(res["suggestedAuth"])
            if arg == "pin":
                Misc.updatePayload(res["suggestedAuth"], payload, pin=pin)
            if arg == "address":
                Misc.updatePayload(res["suggestedAuth"], payload, address={
                    "billingzip": "07205", "billingcity": "Hillside", "billingaddress": "470 Mundet PI", "billingstate": "NJ", "billingcountry": "US"})
            res = rave.Card.charge(payload)
            if res["validationRequired"]:
                rave.Card.validate(res["flwRef"], "12345")
            res = rave.Card.verify(res["txRef"])
            data = res
            print(res["transactionComplete"])
        except RaveExceptions.CardChargeError as e:
            print(e.err["errMsg"])
            print(e.err["flwRef"])
            data = {
                "error": e.err["errMsg"]
            }
        except RaveExceptions.TransactionValidationError as e:
            print(e.err)
            print(e.err["flwRef"])
            data = {
                "error": e.err["errMsg"]
            }
        except RaveExceptions.TransactionVerificationError as e:
            print(e.err["errMsg"])
            print(e.err["txRef"])
            data = {
                "error": e.err["errMsg"]
            }
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404


def preauth_charge(request):
    if request.POST and request.is_ajax():
        inputToken = request.POST.get('inputToken')
        tokenAmount = request.POST.get('tokenAmount')

        payload_for_saved_card = {
            "token": inputToken,
            "amount": tokenAmount,
            "charge_type": "preauth",
            "email": "user@gmail.com",
            "currency": "NGN",
            "country": "NG",
            "phonenumber": "0902620185",
            "firstname": "temi",
            "lastname": "desola",
            "IP": "355426087298442",
        }

        try:
            res = rave.Preauth.charge(payload_for_saved_card, chargeWithToken=True)
            data = res
        except RaveExceptions.TransactionChargeError as e:
            print(e.err["errMsg"])
            print(e.err["flwRef"])
            data = {
                "error": e.err["errMsg"]
            }
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404

def preauth_capture(request):
    if request.POST and request.is_ajax():
        flwRef = request.POST.get('flwRef')
        

        payload = {
            "flwRef": flwRef
        }

        try:
            res = rave.Preauth.capture(payload["flwRef"])
            data = res
        except RaveExceptions.PreauthCaptureError as e:
            print(e.err["errMsg"])
            print(e.err["flwRef"])
            data = {
                "error": e.err["errMsg"]
            }
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404

