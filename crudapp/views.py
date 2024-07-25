from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

#Main menu
def Main(request):
    return render(request, 'Main.html', {})

#Registro
def Registro(request):

    if request.method == ('GET'):
        return render(request, 'access/Registro.html', 
                  {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username= request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('Main')
            except IntegrityError:
                Error= 'Usuario ya existe'
            return render(request, 'access/Registro.html', 
                  {'form': UserCreationForm, 'Error':Error})
        else:
            Error= 'Las password no coinciden'
            return render(request, 'access/Registro.html', 
                  {'form': UserCreationForm, 'Error':Error})
        
#Inicio de sesion
def IniciarSesion(request):
    if request.method == ('GET'):
         return render(request, 'access/login.html', 
                  {'form': AuthenticationForm})
    else:
        try:
            user= authenticate(request, username= request.POST['username'], password = request.POST['password'])
            login(request, user)
            return redirect('Main')
        except AttributeError:
            Error="Los datos no coinciden"
            return render(request, 'access/login.html', 
                  {'form': AuthenticationForm, 'Error': Error})
 
#Cerrar sesion
@login_required
def CerrarSesion(request):
    try:
        logout(request)
        return redirect('Main')
    except:
        pass