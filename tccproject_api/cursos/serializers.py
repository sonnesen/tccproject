from rest_framework import serializers

from cursos.models import Curso, Categoria, Instrutor, Unidade, Atividade,\
    VideoAula, MaterialComplementar, Avaliacao, Arquivo, Questao, Alternativa


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
        fields = ('url', 'titulo', 'unidade', 'video', 'material', 'avaliacao') 
        

class ArquivoSerializer(serializers.HyperlinkedModelSerializer):
    atividade = serializers.SlugRelatedField(
        many=False, 
        read_only=True,
        slug_field='titulo'
    )
    
    class Meta:
        model = Arquivo
        fields = ('url', 'uri', 'atividade', 'tipo')        
         
         
class AvaliacaoSerializer(serializers.HyperlinkedModelSerializer):
    atividade = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Avaliacao
        fields = ('url', 'atividade')        
        
        
class QuestaoSerializer(serializers.HyperlinkedModelSerializer):
    atividade = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Questao
        fields = ('url', 'atividade')        
        
        
class AlternativaSerializer(serializers.HyperlinkedModelSerializer):
    atividade = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Alternativa
        fields = ('url', 'atividade')        


