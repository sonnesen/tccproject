from rest_framework.viewsets import ModelViewSet

from resources.api.serializers import ResourceSerializer
from resources.models import Resource


class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
