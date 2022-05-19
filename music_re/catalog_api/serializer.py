from rest_framework import serializers
from . import models


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genres
        fields = '__all__'


class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tracks
        fields = '__all__'
