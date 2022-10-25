from django.urls import path
from . import views

urlpatterns = [
    path('won_woo',views.won_woo,name='won_woo')
]