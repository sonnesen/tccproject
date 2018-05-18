from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from courses.models import Course
from units.models import Unit


class UnitSerializer(ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    
    class Meta:
        model = Unit
        fields = ('__all__')
