from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='Main'),
    path('Registro/', views.Registro, name='Registro')
]