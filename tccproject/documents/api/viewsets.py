from rest_framework.viewsets import ModelViewSet

from documents.api.serializers import DocumentSerializer
from documents.models import Document


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
