from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='main_index'),
    path('chang_hun',views.chang_hun, name='main_chang_hun'),
    path('ji_hun',views.ji_hun, name='main_ji_hun'),
    path('jun_young',views.jun_young, name='main_jun_young'),
    path('min_jun',views.min_jun, name='main_min_jun'),
    path('won_woo',views.won_woo, name='main_won_woo'),
]