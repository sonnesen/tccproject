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
        
         
class AtividadeSerializer(serializers.ModelSerializer):
    
    arquivo = ArquivoSerializer(many=False)
    
    class Meta:
        model = Atividade
        fields = ('id', 'titulo', 'unidade', 'arquivo') 
        
    def create(self, validated_data):
        arquivo_data = validated_data.pop('arquivo')
        atividade = Atividade.objects.create(**validated_data)
        Arquivo.objects.create(atividade=atividade, **arquivo_data)        
        return atividade    
    
    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.unidade = validated_data.get('unidade', instance.unidade)
        
        arquivo = validated_data.get('arquivo', instance.arquivo)        
        instance.arquivo.uri = arquivo['uri']
        instance.arquivo.tipo = arquivo['tipo']
        
        arquivo = Arquivo.objects.get(id=instance.arquivo.id)
        arquivo.uri = instance.arquivo.uri
        arquivo.tipo = instance.arquivo.tipo
        arquivo.save()        
        
        instance.arquivo = arquivo
        instance.save()
        
        return instance
        
        
class ArquivoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Arquivo
        fields = ('uri', 'tipo')
           
           
class AvaliacaoSerializer(serializers.ModelSerializer):
    atividade = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
     
    class Meta:
        model = Avaliacao
        fields = ('id', 'atividade')        
         
         
class QuestaoSerializer(serializers.ModelSerializer):
    atividade = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
     
    class Meta:
        model = Questao
        fields = ('id', 'atividade')        
         
         
class AlternativaSerializer(serializers.ModelSerializer):
    atividade = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
     
    class Meta:
        model = Alternativa
        fields = ('id', 'atividade')        


