from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from courses.models import Course
from documents.models import Document


class DocumentSerializer(ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    
    class Meta:
        model = Document
        fields = ('__all__')
