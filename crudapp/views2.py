from django.shortcuts import render, redirect
from .models import productos
from .forms import FormProductos

def Producto(request):
    ListaProductos = productos.objects.all()
    return render(request, 'productsviews/Productos.html', {
        'Lista': ListaProductos
    })

def CrearProducto(request):
    if request.method == 'GET':
        return render(request, 'productsviews/CrearProductos.html', {
            'form': FormProductos()
        })
    else:
        form = FormProductos(request.POST)
        if form.is_valid():
            producto_creado = form.save(commit=False)
            producto_creado.user = request.user
            producto_creado.save()
            return redirect('Main')
        else:
            return render(request, 'productsviews/CrearProductos.html', {
                'form': form , 'Error': 'Datos no validos'
            })