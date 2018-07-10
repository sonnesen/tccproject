"""
Módulo alternatives.api.serializers
"""

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from alternatives.models import Alternative
from questions.models import Question


class AlternativeSerializer(ModelSerializer):
    """
    Classe responsável por serializar um objeto do tipo Alternative
    """
    
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all()
    )

    class Meta:
        model = Alternative
        fields = ('__all__')
