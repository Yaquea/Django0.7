from django.contrib import admin
from .models import productos

class pructosvistaadmin(admin.ModelAdmin):
    readonly_fields = ("created", )
    
# Register your models here.
admin.site.register(productos, pructosvistaadmin)