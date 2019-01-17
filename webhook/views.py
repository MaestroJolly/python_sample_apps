import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Log

# Create your views here.
# view for logging webhook requests
@require_http_methods(["GET", "POST"])
@csrf_exempt
def my_webhook_view(request):
  # Retrieve the request's body
  request_json = request.body
  # Do something with request_json
  data = json.loads(request_json)
  print (data)
  if data["event.type"] == "Transfer":
    resp = Log.objects.create(customer_name=data["transfer"]["fullname"], status=data["transfer"]["status"], transaction_type=data["event.type"], amount=data["transfer"]["amount"], account=data["transfer"]["account_number"], narration=data["transfer"]["narration"], currency=data["transfer"]["currency"], created_at=data["transfer"]["date_created"])
  else:
    resp = Log.objects.create(customer_name=data["customer"]["fullName"], customer_email=data["customer"]["email"],status=data["status"], transaction_type=data["event.type"], amount=data["amount"], currency=data["currency"], transaction_ref=data["txRef"], flw_ref=data["flwRef"], created_at=data["customer"]["createdAt"])
  return HttpResponse()

# view for display webhook logs
def webhook_logs(request):
  log_object = Log.objects.all()
  context = {
    "data": log_object
  }
  return render(request, 'webhook/index.html', context)