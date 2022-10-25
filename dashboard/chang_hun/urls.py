from django.urls import path
from . import views

urlpatterns = [
    path('chang_hun',views.chang_hun,name='chang_hun')
]