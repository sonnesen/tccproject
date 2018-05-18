from rest_framework.viewsets import ModelViewSet

from alternatives.api.serializers import AlternativeSerializer
from alternatives.models import Alternative


class AlternativeViewSet(ModelViewSet):
    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializer
