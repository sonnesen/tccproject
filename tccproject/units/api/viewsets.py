from rest_framework.viewsets import ModelViewSet

from units.api.serializers import UnitSerializer
from units.models import Unit


class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
