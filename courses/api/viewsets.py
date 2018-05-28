from rest_framework.viewsets import ModelViewSet

from courses.api.serializers import CourseSerializer
from courses.models import Course


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
