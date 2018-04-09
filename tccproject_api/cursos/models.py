from django.db import models


class Curso(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    criado_em = models.DateField(auto_now=True)
    categoria = models.ForeignKey('Categoria', related_name='cursos', on_delete=models.CASCADE)
    instrutor = models.ForeignKey('Instrutor', related_name='cursos', on_delete=models.CASCADE)
    
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