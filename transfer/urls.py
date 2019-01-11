from django.urls import path
from . import views

urlpatterns = [
    path('', views.transfer, name='transfer'),  #the path for our index view
    path('resolve/', views.resolve_account, name='resolve_account'),
    path('single-transfer/', views.single_transfer, name='single_transfer'),
    path('bulk-transfer/', views.bulk_transfer, name='bulk_transfer')
]