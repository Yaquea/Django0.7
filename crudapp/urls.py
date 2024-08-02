from django.urls import path
from . import views, views2, views3

urlpatterns = [
    path('', views.Main, name='Main'),
    path('Registro/', views.Registro, name='Registro'),
    path('CerrarSesion/', views.CerrarSesion , name= 'CerrarSesion'),
    path('IniciarSesion/', views.IniciarSesion, name='IniciarSesion'),


    #Productos
    path('productos', views2.Producto, name='Productos'),
    path('productos/<int:id>/', views2.ProductoInd, name='Productos indi'),
    path('productos/<int:id>/Actualizar', views2.Actualizar, name='Actualizar'),
    path('productos/<int:id>/Vendido', views2.Vendido, name='Vender'),
    path('productos/creation', views2.CrearProducto, name='Crear Productos'),
    path('productos/Misproductos', views2.OwnProducto, name='Mis Productos'),


    #DogApi
     path('random-dog-image/', views3.RandomDog, name='DogMain'),
]