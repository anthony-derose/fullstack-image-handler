from rest_framework import serializers
from .models import ImageApp

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageApp 
        fields = ('id', 'image')