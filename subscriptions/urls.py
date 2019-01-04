from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions_view, name='subscriptions'),  #the path for our index view

]