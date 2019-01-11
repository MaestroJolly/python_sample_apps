from django.urls import path
from . import views

urlpatterns = [
    path('', views.splitpayment, name='splitpayment'),  #the path for our index view
    path('list_banks/', views.list_banks, name='list_banks'), 
    path('pay/', views.pay, name='pay')
    # path('cancel_sub/', views.cancel_sub, name='cancel_sub'),
    # path('activate_sub/', views.activate_sub, name='activate_sub'),

]