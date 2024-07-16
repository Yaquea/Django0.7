from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Main menu
def Main(request):
    return render(request, 'Main.html', {})


#Registro
def Registro(request):

    if request.method == ('GET'):
        return render(request, 'Registro.html', 
                  {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username= request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('Main')
            except:
                Error= 'Usuario ya existe'
            return render(request, 'Registro.html', 
                  {'form': UserCreationForm, 'Error':Error})
        else:
            Error= 'Las password no coinciden'
            return render(request, 'Registro.html', 
                  {'form': UserCreationForm, 'Error':Error})
            
