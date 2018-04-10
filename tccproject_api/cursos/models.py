from django.db import models


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
        
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False)
    
    class Meta:
        ordering = ('nome', )
        
    def __str__(self):
        return self.nome
    
class Instrutor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    contato = models.CharField(max_length=100, null=False)
    resumo = models.TextField(max_length=200, null=False)
    
    class Meta:
        ordering = ('nome', )
        
    def __str__(self):
        return self.nome
    

class Unidade(models.Model):
    titulo = models.CharField('Título', max_length=100, null=False)
    curso = models.ForeignKey('Curso', related_name='unidades', on_delete=models.CASCADE)
        
    def __str__(self):
        return self.titulo
    
    
class Atividade(models.Model):
    titulo = models.CharField('Título', max_length=100, null=False)
    unidade = models.ForeignKey('Unidade', related_name='atividades', on_delete=models.CASCADE)
    
    TIPO_ATIVIDADE = (
        (0, 'Vídeo'),
        (1, 'Material Complementar'),
        (2, 'Avaliação')
    )
    
    tipo = models.IntegerField(choices=TIPO_ATIVIDADE, default=0)
    
    def __str__(self):
        return self.titulo
    
class Recurso():
    uri = models.URLField()
        
class VideoAula(Atividade, Recurso):
    
    def __init__(self):
        self.tipo = Atividade.TIPO_ATIVIDADE(0)
        
    class Meta:
        proxy = True
    

class MaterialComplementar(Atividade, Recurso):
    
    def __init__(self):
        self.tipo = Atividade.TIPO_ATIVIDADE(1)
        
    class Meta:
        proxy = True
        
class Avaliacao(Atividade):
    
    def __init__(self):
        self.tipo = Atividade.TIPO_ATIVIDADE(2)
        
    class Meta:
        proxy = True