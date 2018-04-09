from rest_framework import viewsets, permissions

from cursos.permissions import IsAdminOrReadOnly
from cursos.models import Curso, Categoria, Instrutor
from cursos.serializers import CursoSerializer, CategoriaSerializer,\
    InstrutorSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly)
    
class CategoriaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly)
    
    
class InstrutorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly)    
    
