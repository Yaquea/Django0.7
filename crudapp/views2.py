from django.shortcuts import render, redirect, get_object_or_404
from django.urls import NoReverseMatch
from .models import productos
from .forms import FormProductos
from django.core.exceptions import ObjectDoesNotExist

#Muestra todos los productos hechos por cualquier usuario
def Producto(request):
    if request.method == ('POST'):
        try:
             Buscar = productos.objects.filter(title= request.POST['Busqueda'])
             return render(request, 'productsviews/ResultadoProducto.html', {'Busqueda': Buscar})
        except ObjectDoesNotExist:
            ListaProductos = productos.objects.filter(user=request.user)
            return render(request, 'productsviews/ResultadoProducto.html', {'Error':'El producto que buscas no existe'})   
    else:
        ListaProductos = productos.objects.all()
        return render(request, 'productsviews/Productos.html', {'Lista': ListaProductos, })


#Muestra solo los productos creados por personas
def OwnProducto(request):
    
    if request.method == ('POST'):
        try:
             Buscar = productos.objects.filter(title= request.POST['Busqueda'])
             return render(request, 'productsviews/ResultadoProducto.html', {'Busqueda': Buscar})
        except ObjectDoesNotExist:
            ListaProductos = productos.objects.filter(user=request.user)
            return render(request, 'productsviews/OwnProductos.html', {'Error':'El producto que buscas no existe'})   
    else:
        ListaProductos = productos.objects.filter(user=request.user)
        return render(request, 'productsviews/OwnProductos.html', {'Lista': ListaProductos, })
    

def ProductoInd(request, id):
    if request.method == 'GET':
        Producto = get_object_or_404(productos, pk=id)
        ProductoPersonal = productos.objects.filter(pk=id, user=request.user)
        if ProductoPersonal.exists():
            return render(request, 'productsviews/Productosind.html', {'producto': Producto, 'Value': True})
        else:
            return render(request, 'productsviews/Productosind.html', {'producto': Producto, 'Value': False})
    else:
        ProductoPersonal = productos.objects.filter(pk=id, user=request.user)
        if ProductoPersonal.exists():
            Producto = get_object_or_404(productos, pk=id)
            ProductoLlamado = FormProductos(instance=Producto)
            return render(request, 'productsviews/Actualizar.html', {'producto': Producto, 'form': ProductoLlamado})
        else:
            Producto = get_object_or_404(productos, pk=id)
            return render(request, 'productsviews/Productosind.html', {'producto': Producto, 'Error': 'El producto no es propio', 'Value': False})

def Actualizar(request, id):
    if request.method == 'POST':

        ProductoPersonal = get_object_or_404(productos, pk=id, user=request.user)
        NewForm = FormProductos(request.POST, instance=ProductoPersonal)
        if NewForm.is_valid():
            NewForm.save()
            return redirect('Mis Productos')
        else:
            return render(request, 'productsviews/Actualizar.html', {'producto': ProductoPersonal, 'form': NewForm, 'Error': 'Datos no validos'})
    else:
        ProductoPersonal = get_object_or_404(productos, pk=id, user=request.user)
        NewForm = FormProductos(instance=ProductoPersonal)
        return render(request, 'productsviews/Actualizar.html', {'productoi': ProductoPersonal, 'form': NewForm})
        



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

