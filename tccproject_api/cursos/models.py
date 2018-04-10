from django.db import models
from abc import abstractproperty


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
    
    TIPO_ATIVIDADE = ((0, 'Vídeo'), (1, 'Material Complementar'), (2, 'Avaliação'))
    
    tipo = models.IntegerField(choices=TIPO_ATIVIDADE, default=0)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'atividade'
    

class VideoAula(models.Model):
    uri = models.URLField()
    atividade = models.OneToOneField('Atividade', on_delete=models.CASCADE, primary_key=True)
    
    def __init__(self, uri=None, atividade=None):
        self.atividade.tipo = 0
        self.uri = uri
        self.atitivade = atividade
        
    class Meta:
        db_table = 'video_aula'
        

class MaterialComplementar(models.Model):
    uri = models.URLField()
    atividade = models.OneToOneField('Atividade', on_delete=models.CASCADE, primary_key=True)
    
    def __init__(self, uri=None, atividade=None):
        self.atividade.tipo = 1
        self.uri = uri
        self.atitivade = atividade
        
    class Meta:
        db_table = 'material_compl'
        
        
class Avaliacao(models.Model):
    atividade = models.OneToOneField('Atividade', on_delete=models.CASCADE, primary_key=True)
    
    def __init__(self):
        self.atividade.tipo = 2

    class Meta:
        db_table = 'avaliacao'
