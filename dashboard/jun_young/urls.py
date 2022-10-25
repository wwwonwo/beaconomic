from django.urls import path
from . import views

urlpatterns = [
    path('jun_young',views.jun_young,name='jun_young')
]