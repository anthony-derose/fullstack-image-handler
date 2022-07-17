from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImageSerializer
from .models import ImageApp

# Create your views here.
class ImageAppView(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = ImageApp.objects.all()
