from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def Producto(request):
    return render(request, 'Productos.html', {})