from django.db import models

from instrutores.models import Instrutor


class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False)
    
    
class Curso(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    criado_em = models.DateField(auto_now=True)
    categoria = models.ForeignKey(Categoria, related_name='cursos', on_delete=models.CASCADE)
    instrutor = models.ForeignKey(Instrutor, related_name='cursos', on_delete=models.CASCADE)
    palavras_chave = models.TextField(max_length=255, null=True)
    
    
class Unidade(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    curso = models.ForeignKey(Curso, related_name='unidades', on_delete=models.CASCADE)
    

class Atividade(models.Model):
    unidade = models.ForeignKey(Unidade, related_name='atividades', on_delete=models.CASCADE)    


class Questao(models.Model):
    atividade = models.ForeignKey(Atividade, related_name='questoes', on_delete=models.CASCADE)
    

class Material(models.Model):    
    unidade = models.ForeignKey(Atividade, related_name='materiais', on_delete=models.CASCADE)    