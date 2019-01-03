from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests

# Create your views here.
def subscriptions_view(request):
    url = 'https://ravesandboxapi.flutterwave.com/v2/gpx/subscriptions/query?seckey=FLWSECK-a18ca169cb007a93db4479aff683a387-X'

    sub_info = requests.get(url).json()

    subscriptions = {
        'status': sub_info['status'],
        'message': sub_info['message']
        # 'subs': sub_info['plansubscriptions']
    }

    context = {'subscriptions': subscriptions}
    return render(request, 'subscriptions/index.html', context) #returns the index.html template
