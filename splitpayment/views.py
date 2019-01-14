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
rave = Rave(RAVE_PUBLIC_KEY, RAVE_SECRET_KEY, usingEnv = True)

@require_http_methods(["GET", "POST"])
@csrf_exempt
def splitpayment(request):
    data = list_banks()
    context = {
        'banks': data
    }
    return render(request, 'splitpayment/index.html', context)


def list_banks():
    RAVE_PUBLIC_KEY = "FLWPUBK-f54d8d24292e377a71620bd82a8bb17c-X"
    url = 'https://ravesandboxapi.flutterwave.com/v2/banks/NG?public_key=' + RAVE_PUBLIC_KEY
    bank_lists = requests.get(url).json()
    banks = bank_lists["data"]["Banks"]
    return banks


def pay(request):
    if request.POST and request.is_ajax():
        accountnumber = request.POST.get('accountnumber')
        accountbank = request.POST.get('accountbank')
        subaccounts = request.POST.get('subaccounts')
        

        payload = {
            'accountbank': accountbank,
            'accountnumber': accountnumber,
            'amount': '300',
            'email': 'test@test.com',
            'phonenumber': '08123456789',
            'currency': 'NGN',
            'country': 'NG',
            'IP': '355426087298442',
            'subaccounts': subaccounts
        }
        print(payload)
        try:
            res = rave.Account.charge(payload)
            if res["authUrl"]:
                print(res["authUrl"])
            elif res["validationRequired"]:
                rave.Account.validate(res["flwRef"], "12345")

            res = rave.Account.verify(res["txRef"])
        except RaveExceptions.AccountChargeError as e:
            print(e.err)
            print(e.err["flwRef"])

        except RaveExceptions.TransactionValidationError as e:
            print(e.err)
            print(e.err["flwRef"])

        except RaveExceptions.TransactionVerificationError as e:
            print(e.err["errMsg"])
            print(e.err["txRef"])
        data = res
        print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404
