from django.urls import path
from . import views

urlpatterns = [
    path('min_jun',views.min_jun,name='min_jun')
]