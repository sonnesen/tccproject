from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from units.models import Unit
from videos.models import Video


class VideoSerializer(ModelSerializer):
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
    
    class Meta:
        model = Video
        fields = ('__all__')
