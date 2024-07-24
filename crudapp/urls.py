from django.urls import path
from . import views
from . import views2

urlpatterns = [
    path('', views.Main, name='Main'),
    path('Registro/', views.Registro, name='Registro'),
    path('CerrarSesion/', views.CerrarSesion , name= 'CerrarSesion'),
    path('IniciarSesion/', views.IniciarSesion, name='IniciarSesion'),


    #Productos
    path('productos', views2.Producto, name='Productos'),
    path('productos/<int:id>/', views2.ProductoInd, name='Productos indi'),
    path('productos/<int:id>/Actualizar', views2.Actualizar, name='Actualizar'),
    path('productos/creation', views2.CrearProducto, name='Crear Productos'),
    path('productos/Misproductos', views2.OwnProducto, name='Mis Productos'),
]