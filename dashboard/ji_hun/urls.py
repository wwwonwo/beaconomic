from django.urls import path
from . import views

urlpatterns = [
    path('ji_hun',views.ji_hun,name='ji_hun')
]