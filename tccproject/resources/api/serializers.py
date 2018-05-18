from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from activities.models import Activity
from resources.models import Resource


class ResourceSerializer(ModelSerializer):
    activity = serializers.PrimaryKeyRelatedField(queryset=Activity.objects.all())
    
    class Meta:
        model = Resource
        fields = ('__all__')
