"""
Módulo alternatives.api.viewsets
"""

from rest_framework.viewsets import ModelViewSet

from alternatives.api.serializers import AlternativeSerializer
from alternatives.models import Alternative


class AlternativeViewSet(ModelViewSet):
    """
    Classe responsável pela visualização de um objeto do tipo Alternative
    """

    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializer
