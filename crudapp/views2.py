from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import FormProductos

def Producto(request):
    return render(request, 'productsviews/Productos.html', {

    })

def CrearProducto(request):
    if request.method == ('GET'):
        return render(request, 'productsviews/CrearProductos.html', {
        'form': FormProductos
    })
    else: 
        print(request.POST)
        return redirect('Main')
    