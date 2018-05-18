from rest_framework.viewsets import ModelViewSet

from activities.api.serializers import ActivitySerializer
from activities.models import Activity


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
