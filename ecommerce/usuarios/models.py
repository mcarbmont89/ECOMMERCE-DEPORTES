from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True,blank=True,default="/default.jpeg")
