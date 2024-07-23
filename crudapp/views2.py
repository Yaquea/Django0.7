from django.shortcuts import render, redirect, get_object_or_404
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
    

#Crea una view de cualquier producto individual
def ProductoInd(request, id):
    if request.method == ('GET'):
        Producto = get_object_or_404(productos, pk = id)
        ProductoPersonal = productos.objects.filter(pk= id, user = request.user)
        if ProductoPersonal.exists():
            ProductoLlamado = FormProductos(instance= Producto)
            return render(request, 'productsviews/Productosind.html', {'producto': Producto, 'Value': True})
        else:
            ProductoLlamado = FormProductos(instance= Producto)
            return render(request, 'productsviews/Productosind.html', {'producto': Producto, 'Value': False})
    else:
        Producto = get_object_or_404(productos, pk = id)
        ProductoPersonal = productos.objects.filter(pk= id, user = request.user)
        if ProductoPersonal.exists():
            ProductoLlamado = FormProductos(instance= Producto)
            return render(request, 'productsviews/Actualizar.html', {'producto': Producto, 'form':ProductoLlamado})
        else: 
            Producto = get_object_or_404(productos, pk = id)
            ProductoLlamado = FormProductos(instance= Producto)
            return render(request, 'productsviews/Productosind.html', {'producto': Producto, 'Error': 'El producto no es propio', 'Value': False})


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

