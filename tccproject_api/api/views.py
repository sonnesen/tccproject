from rest_framework import viewsets, permissions

from api.models import Curso, Categoria, Instrutor, Unidade, Atividade, Arquivo,\
    Avaliacao, Questao, Alternativa
from api.permissions import IsAdminOrReadOnly
from api.serializers import CursoSerializer, CategoriaSerializer, \
    InstrutorSerializer, UnidadeSerializer, AtividadeSerializer,\
    ArquivoSerializer


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
     
 
class UnidadeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
     
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly)
     
class AtividadeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
     
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly)    
     

class ArquivoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
     
    queryset = Arquivo.objects.all()
    serializer_class = ArquivoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly)    
     

class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
     
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly)    
     

class QuestaoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
     
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly)    
     

class AlternativaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
     
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly)    
     



