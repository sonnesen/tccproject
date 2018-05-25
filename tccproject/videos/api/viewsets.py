from rest_framework.viewsets import ModelViewSet

from videos.api.serializers import VideoSerializer
from videos.models import Video


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
