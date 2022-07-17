from django.db import models
from django.db.models import Model

class ImageApp(Model):
    image = models.ImageField()
    
