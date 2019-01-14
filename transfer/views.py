import requests
import json
import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from python_rave import Rave, RaveExceptions

RAVE_PUBLIC_KEY = os.getenv('RAVE_PUBLIC_KEY')
RAVE_SECRET_KEY = os.getenv('RAVE_SECRET_KEY')
rave = Rave(RAVE_PUBLIC_KEY, RAVE_SECRET_KEY, usingEnv = True)

# View that renders the transfer template and also dislays the list of banks.
@require_http_methods(["GET", "POST"])
@csrf_exempt
def transfer(request):
    url = 'https://ravesandboxapi.flutterwave.com/v2/banks/NG?public_key=' + RAVE_PUBLIC_KEY
    bank_lists = requests.get(url).json()
    banks = bank_lists["data"]["Banks"]
    context = {
        "banks": banks
    }
    return render(request, 'transfer/index.html', context)

# View that resolves customer's account number.
def resolve_account(request):
    url = 'https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/resolve_account'
    if request.POST and request.is_ajax():
        payload = {
            "recipientaccount": request.POST.get("recipientaccount"),
            "destbankcode": request.POST.get("destbankcode"),
            "PBFPubKey": RAVE_PUBLIC_KEY
        }
        data = requests.post(url, payload)
        print(data)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404

# View that initiate single transfer.
def single_transfer(request):
    if request.POST and request.is_ajax():
        try:
            res = rave.Transfer.initiate({
            "account_bank": request.POST.get("account_code"),
            "account_number": request.POST.get("account_bank"),
            "amount": request.POST.get("single_amount"),
            "beneficiary_name": request.POST.get("account_name"),
            "narration": request.POST.get("narration"),
            "currency": "NGN",
            "meta": [{
                "metaname": "flightID",
                "metavalue": "AP1234"
            }]
            })

            print(res)
            data = json.dumps(res)
        except RaveExceptions.IncompletePaymentDetailsError as e:
            print(e)

        except RaveExceptions.InitiateTransferError as e:
            print(e.err)

        except RaveExceptions.TransferFetchError as e:
            print(e.err)

        except RaveExceptions.ServerError as e:
            print(e.err)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404

# View that initiate bulk transfer.
def bulk_transfer(request):
    if request.POST and request.is_ajax():
        post_data = request.POST.get('recipientslist')
        item_data = json.loads(post_data)
        try:
            res2 = rave.Transfer.bulk({
            "title": request.POST.get("title"),
            "bulk_data": item_data
            })
            print(res2)
            data = json.dumps(res2)
        except RaveExceptions.IncompletePaymentDetailsError as e:
            print(e)

        except RaveExceptions.InitiateTransferError as e:
            print(e.err)

        except RaveExceptions.TransferFetchError as e:
            print(e.err)

        except RaveExceptions.ServerError as e:
            print(e.err)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404