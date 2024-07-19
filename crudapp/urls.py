from django.urls import path
from . import views
from . import views2

urlpatterns = [
    path('', views.Main, name='Main'),
    path('Registro/', views.Registro, name='Registro'),
    path('CerrarSesion/', views.CerrarSesion , name= 'CerrarSesion'),
    path('IniciarSesion/', views.IniciarSesion, name='IniciarSesion'),
]