from django.shortcuts import render, redirect
from .models import productos
from .forms import FormProductos

#Muestra todos los productos hechos por cualquier usuario
def Producto(request):
    ListaProductos = productos.objects.all()
    return render(request, 'productsviews/Productos.html', {
        'Lista': ListaProductos
    })

#Esta view permite crear productos
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

#Muestra solo los productos creados por personas
def OwnProducto(request):
    ListaProductos = productos.objects.filter(user=request.user)
    return render(request, 'productsviews/OwnProductos.html', {
        'Lista': ListaProductos
    })