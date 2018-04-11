from enum import unique, IntEnum

from django.db import models
from unittest.util import _MAX_LENGTH


class Curso(models.Model):
    titulo = models.CharField('Título', max_length=100, null=False)
    criado_em = models.DateField('Data de criação', auto_now=True)
    categoria = models.ForeignKey('Categoria', related_name='cursos', on_delete=models.CASCADE)
    instrutor = models.ForeignKey('Instrutor', related_name='cursos', on_delete=models.CASCADE)
    palavras_chave = models.CharField('Palavras-Chave', max_length=100, null=True)
        
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('criado_em',)
        db_table = 'curso'
        
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ('nome', )
        db_table = 'categoria'        
    
    
class Instrutor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    contato = models.CharField(max_length=100, null=False)
    resumo = models.TextField(max_length=200, null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ('nome', )
        db_table = 'instrutor'
        
    
class Unidade(models.Model):
    titulo = models.CharField('Título', max_length=100, null=False)
    curso = models.ForeignKey('Curso', related_name='unidades', on_delete=models.CASCADE)
        
    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'unidade'
    
    
class Atividade(models.Model):
    titulo = models.CharField('Título', max_length=100, null=False)
    unidade = models.ForeignKey('Unidade', related_name='atividades', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'atividade'
    

@unique
class TipoArquivo(IntEnum):
    VIDEO = 1
    MATERIAL = 2
    
    @classmethod
    def tipos(cls):
        tipos = []
        for chave, valor in TipoArquivo.__members__.items():
            tipo = (chave, valor)
            tipos.append(tipo)
        return tipos
    
    
class Arquivo(models.Model):
    uri = models.URLField(max_length=2000)
    atividade = models.OneToOneField('Atividade', related_name='arquivo', on_delete=models.CASCADE)
    tipo = models.SmallIntegerField(choices=TipoArquivo.tipos())
    
    class Meta:
        db_table = 'video_aula'
       
        
class Avaliacao(models.Model):
    unidade = models.ForeignKey('Unidade', related_name='avaliacoes', on_delete=models.CASCADE, null=True)
     
    class Meta:
        db_table = 'avaliacao'

class Questao(models.Model):
    enunciado = models.TextField(max_length=500)
    avaliacao = models.ForeignKey('Avaliacao', related_name='questoes', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'questao'
        

class Alternativa(models.Model):
    descricao = models.TextField(max_length=500)
    justificativa = models.TextField(max_length=500)
    questao = models.OneToOneField('Questao', related_name='alternativa', on_delete=models.CASCADE)
    correta = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'alternativa'