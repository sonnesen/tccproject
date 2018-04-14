from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Unidade, Curso, Categoria, Instrutor


class UnidadeViewTestCase(TestCase):
    
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Programação')
        self.instrutor = Instrutor.objects.create(nome='Fulano de Tal',
                                                  contato='fulano@test.com',
                                                  resumo='Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.')
        
        self.curso = Curso.objects.create(titulo='Java parte 1: Primeiros passos',
                                          categoria=self.categoria,
                                          instrutor=self.instrutor,
                                          palavras_chave='java iniciante')
        
        self.unidade = Unidade.objects.create(titulo='Descrição',
                                              curso=self.curso)
        
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/unidades/'
        
    def test_api_can_get_all_unidade(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_unidade(self):
        self.data = {
            'titulo': 'Unidade 1',
            'curso': self.curso.id
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_not_create_unidade(self):
        self.client.logout()
        self.data = {
            'titulo': 'Unidade 1',
            'curso': self.curso.id
        }        
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_get_unidade(self):
        self.response = self.client.get('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
        
    def test_api_can_not_get_unidade(self):
        self.response = self.client.get('{}{}/'.format(self.url, 9999), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_api_can_update_unidade(self):
        self.data = {
            'titulo': 'Nova Unidade 1',
            'curso': self.curso.id
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)       
        
    def test_api_can_not_update_unidade(self):
        self.client.logout()
        self.data = {
            'titulo': 'Nova Unidade 1',
            'curso': self.curso.id
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_delete_unidade(self):
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_api_can_not_delete_unidade(self):
        self.client.logout()
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
