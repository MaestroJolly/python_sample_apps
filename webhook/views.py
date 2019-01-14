import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
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

# def my_webhook_view(request):

#   if request.POST and request.is_ajax():
#     # todo_items = ['Mow Lawn', 'Buy Groceries']
#     todo_items = {
#       "recipientaccount" : request.POST.get("recipientaccount"),
#       "destbankcode" : request.POST.get("destbankcode")
#     }
#     data = json.dumps(todo_items)
#     return HttpResponse(data, content_type='application/json')
#   else:
#       raise Http404