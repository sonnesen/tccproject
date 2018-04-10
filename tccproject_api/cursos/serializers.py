from rest_framework import serializers

from cursos.models import Curso, Categoria, Instrutor, Unidade, Atividade,\
    VideoAula, MaterialComplementar


class CursoSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Curso
        fields = ('url', 'titulo', 'criado_em', 'categoria', 'instrutor', 'palavras_chave', 'unidades')
        

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Categoria
        fields = ('url', 'nome')
        

class InstrutorSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Instrutor
        fields = ('url', 'nome', 'contato', 'resumo')
        
        
class UnidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidade
        fields = ('url', 'titulo', 'curso')
        
        
class AtividadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atividade
        fields = ('url', 'titulo', 'unidade') 
        

class VideoAulaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoAula
        fields = ('url', 'descricao', 'uri', 'atividade')        
         
         
class MaterialComplementarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaterialComplementar
        fields = ('url', 'descricao', 'uri', 'atividade')


