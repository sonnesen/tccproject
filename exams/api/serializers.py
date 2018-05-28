from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from exams.models import Exam
from units.models import Unit


class ExamSerializer(ModelSerializer):
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
    
    class Meta:
        model = Exam
        fields = ('__all__')
