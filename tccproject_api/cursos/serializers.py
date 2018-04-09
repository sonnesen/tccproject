from rest_framework import serializers

from cursos.models import Curso, Categoria, Instrutor


class CursoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Curso
        fields = ('url', 'titulo', 'criado_em', 'categoria', 'instrutor')
        

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ('url', 'nome')
        

class InstrutorSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Instrutor
        fields = ('url', 'nome', 'contato', 'resumo')
        
        