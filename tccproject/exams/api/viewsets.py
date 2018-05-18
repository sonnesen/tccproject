from rest_framework.viewsets import ModelViewSet

from exams.api.serializers import ExamSerializer
from exams.models import Exam


class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
