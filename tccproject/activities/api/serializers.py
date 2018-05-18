from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from activities.models import Activity
from units.models import Unit


class ActivitySerializer(ModelSerializer):
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
    
    class Meta:
        model = Activity
        fields = ('__all__')
