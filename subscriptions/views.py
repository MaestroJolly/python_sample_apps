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


@require_http_methods(["GET", "POST"])
@csrf_exempt
def subscriptions(request):
    return render(request, 'subscriptions/index.html', context=None)


def list_all(request):
    if request.GET and request.is_ajax():
        try:
            res2 = rave.Subscriptions.allSubscriptions()
        except RaveExceptions.PlanStatusError as e:
            print(e.err["errMsg"])
            print(e.err["flwRef"])
        data = res2
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404



def fetch_sub(request):
    if request.POST and request.is_ajax():
        sub_id = request.POST.get('subid')
        sub_email = request.POST.get('subemail')
        try:
            res2 = rave.Subscriptions.fetchSubscription(sub_id, sub_email)
        except RaveExceptions.PlanStatusError as e:
            print(e.err["errMsg"])
            print(e.err["flwRef"])
        data = res2
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404


def cancel_sub(request):
    if request.POST and request.is_ajax():
        sub_id = request.POST.get('subid')
        try:
            res2 = rave.Subscriptions.cancelSubscription(sub_id)
        except RaveExceptions.PlanStatusError as e:
            print(e.err["errMsg"])
            print(e.err["flwRef"])
        data = res2
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404

def activate_sub(request):
    if request.POST and request.is_ajax():
        sub_id = request.POST.get('subid')
        try:
            res2 = rave.Subscriptions.activateSubscription(sub_id)
        except RaveExceptions.PlanStatusError as e:
            print(e.err["errMsg"])
            print(e.err["flwRef"])
        data = res2
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404
