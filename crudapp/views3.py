from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

@login_required
def RandomDog(request):

    if request.method == 'GET':

        url= "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            dog_image_url = data['message']
        else:
            dog_image_url = None
    
        return render(request, 'DogApi/DogApi.html', {'Api': dog_image_url})
    else:

        Key= request.POST['Busqueda']
        url = "https://dog.ceo/api/breed/" + Key + "/images/random"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            dog_image_url = data['message']
        else:
            dog_image_url = None
    
        return render(request, 'DogApi/DogApi.html', {'Api': dog_image_url})