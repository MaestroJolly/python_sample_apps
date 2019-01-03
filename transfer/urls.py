from django.urls import path
from . import views

urlpatterns = [
    path('', views.transfer, name='transfer'),  #the path for our index view
]