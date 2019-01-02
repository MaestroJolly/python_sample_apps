import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET", "POST"])
@csrf_exempt
def my_webhook_view(request):
  # Retrieve the request's body
  request_json = request.body

  # Do something with request_json
  print (request_json)
  return HttpResponse()