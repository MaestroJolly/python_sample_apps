from django.urls import path
from . import views

urlpatterns = [
    path('', views.preauth, name='preauth'), #the path for our index view
    path('card_charge/', views.card_charge, name='card_charge'),  
    path('preauth_charge/', views.preauth_charge, name='preauth_charge'),
    path('preauth_capture/', views.preauth_capture, name='preauth_capture')

]