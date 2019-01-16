from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'), #the path for our index view
    path('list_all/', views.list_all, name='list_all'),
    path('fetch_sub/', views.fetch_sub, name='fetch_sub'),
    path('cancel_sub/', views.cancel_sub, name='cancel_sub'),
    path('activate_sub/', views.activate_sub, name='activate_sub'),

]