from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class productos(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    onsale = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title + ' creado por: ' + self.user.username
