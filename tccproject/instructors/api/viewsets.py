from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from instructors.api.serializers import InstructorSerializer
from instructors.models import Instructor


class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
