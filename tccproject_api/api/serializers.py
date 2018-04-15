from rest_framework import serializers

from api.models import Categoria, Unidade, Atividade, Arquivo, Avaliacao,\
    Questao, Alternativa
from api.models import Curso, Instrutor


class CursoSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'criado_em', 'categoria', 'instrutor', 'palavras_chave')
        read_only_fields = ('criado_em',)
        

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ('id', 'nome')
         
 
class InstrutorSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Instrutor
        fields = ('id', 'nome', 'contato', 'resumo')
         
         
class UnidadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Unidade
        fields = ('id', 'titulo', 'curso')
        
        
class ArquivoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Arquivo
        fields = ('id', 'tipo', 'uri', 'atividade')
        
                 
class AtividadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Atividade
        fields = ('id', 'titulo', 'unidade') 
           
           
class AvaliacaoSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Avaliacao
        fields = ('id', 'unidade')        
         
         
class QuestaoSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Questao
        fields = ('id', 'enunciado', 'avaliacao')
         
         
class AlternativaSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Alternativa
        fields = ('id', 'descricao', 'justificativa', 'questao', 'correta')        

