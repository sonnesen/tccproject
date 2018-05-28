from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from exams.models import Exam
from questions.models import Question


class QuestionSerializer(ModelSerializer):
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())
    
    class Meta:
        model = Question
        fields = ('__all__')
