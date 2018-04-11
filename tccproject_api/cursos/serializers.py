from rest_framework import serializers

from cursos.models import Categoria, Unidade, Atividade, Arquivo
from cursos.models import Curso, Instrutor


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
        
         
class ArquivoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Arquivo
        fields = ('uri', 'tipo')
                 
                 
class AtividadeSerializer(serializers.HyperlinkedModelSerializer):
    arquivo = ArquivoSerializer(many=False)
    
    class Meta:
        model = Atividade
        fields = ('url', 'titulo', 'unidade', 'arquivo') 
        
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
        
        
           
           
# class AvaliacaoSerializer(serializers.HyperlinkedModelSerializer):
#     atividade = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
#     
#     class Meta:
#         model = Avaliacao
#         fields = ('url', 'atividade')        
#         
#         
# class QuestaoSerializer(serializers.HyperlinkedModelSerializer):
#     atividade = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
#     
#     class Meta:
#         model = Questao
#         fields = ('url', 'atividade')        
#         
#         
# class AlternativaSerializer(serializers.HyperlinkedModelSerializer):
#     atividade = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
#     
#     class Meta:
#         model = Alternativa
#         fields = ('url', 'atividade')        


