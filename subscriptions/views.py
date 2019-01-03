import requests
from django.shortcuts import render
from django.http import HttpResponse
from python_rave import Rave, RaveExceptions, Misc

# Create your views here.
def subscriptions_view(request):
    url = 'https://ravesandboxapi.flutterwave.com/v2/gpx/subscriptions/query?seckey=FLWSECK-a18ca169cb007a93db4479aff683a387-X'

    sub_info = requests.get(url).json()

    subscriptions = {
        'status': sub_info['status'],
        'message': sub_info['message']
        # 'subs': sub_info['plansubscriptions']
    }
    # charge()
    context = {'subscriptions': subscriptions}
    return render(request, 'subscriptions/index.html', context) #returns the index.html template

def charge():
  rave = Rave("FLWPUBK-ba0a57153f497c03bf34a9e296aa9439-X", "FLWSECK-327b3874ca8e75640a1198a1b75c0b0b-X", usingEnv = False)

  # Payload with pin
  payload = {
    "cardno": "5438898014560229",
    "cvv": "890",
    "expirymonth": "09",
    "expiryyear": "19",
    "amount": "10",
    "email": "user@gmail.com",
    "phonenumber": "0902620185",
    "firstname": "temi",
    "lastname": "desola",
    "IP": "355426087298442",
  }

  try:
      res = rave.Card.charge(payload)
      print(res)
      print (res["suggestedAuth"])
      if res["suggestedAuth"]:
          arg = Misc.getTypeOfArgsRequired(res["suggestedAuth"])
          if arg == "pin":
              Misc.updatePayload(res["suggestedAuth"], payload, pin="3310")
          if arg == "address":
              Misc.updatePayload(res["suggestedAuth"], payload, address= {"billingzip": "07205", "billingcity": "Hillside", "billingaddress": "470 Mundet PI", "billingstate": "NJ", "billingcountry": "US"})
          
          res = rave.Card.charge(payload)

      if res["validationRequired"]:
          res = rave.Card.validate(res["flwRef"], "12345")
          print (res)

      res = rave.Card.verify(res["txRef"])
      print(res["transactionComplete"])
      print(res)

  except RaveExceptions.CardChargeError as e:
      print(e.err["errMsg"])
      print(e.err["flwRef"])

  except RaveExceptions.TransactionValidationError as e:
      print(e.err)
      print(e.err["flwRef"])

  except RaveExceptions.TransactionVerificationError as e:
      print(e.err["errMsg"])
      print(e.err["txRef"])
