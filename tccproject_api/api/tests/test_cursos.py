from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Curso, Categoria, Instrutor


class CursoViewTestCase(TestCase):
    
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Programação')
        self.instrutor = Instrutor.objects.create(nome='Fulano de Tal',
                                 contato='fulano@test.com',
                                 resumo='Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.')
        
        self.curso = Curso.objects.create(
            titulo='Java parte 1: Primeiros passos',
            categoria=self.categoria,
            instrutor=self.instrutor,
            palavras_chave='java iniciante')
        
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/cursos/'
        
    def test_api_can_get_all_curso(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_curso(self):
        self.data = {
            'titulo': 'Java parte 2: Introdução à Orientação a Objetos',
            'categoria': self.categoria.id,
            'instrutor': self.instrutor.id,
            'palavras_chave': 'java intermediário',
            'unidades': {}
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
         
    def test_api_can_not_create_curso(self):
        self.client.logout()
        self.data = {
            'titulo': 'Java parte 2: Introdução à Orientação a Objetos',
            'categoria': self.categoria.id,
            'instrutor': self.instrutor.id,
            'palavras_chave': 'java intermediário',
            'unidades': {}
        }        
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_get_curso(self):
        self.response = self.client.get('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
        
    def test_api_can_not_get_curso(self):
        self.response = self.client.get('{}{}/'.format(self.url, 9999), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_api_can_update_curso(self):        
        self.data = {
            'titulo': 'Java parte 2: Introdução à Orientação a Objetos',
            'categoria': self.categoria.id,
            'instrutor': self.instrutor.id,
            'palavras_chave': 'java intermediário orientação objetos',
            'unidades': {}
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
         
    def test_api_can_not_update_curso(self):
        self.client.logout()        
        self.data = {
            'titulo': 'Java parte 2: Introdução à Orientação a Objetos',
            'categoria': self.categoria.id,
            'instrutor': self.instrutor.id,
            'palavras_chave': 'java intermediário orientação objetos',
            'unidades': {}
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_delete_curso(self):
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_api_can_not_delete_curso(self):
        self.client.logout()
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
