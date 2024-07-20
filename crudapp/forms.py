from django.forms import ModelForm
from .models import productos

class FormProductos(ModelForm):
    class Meta:
        model = productos
        fields = ['title', 'description', 'price']
