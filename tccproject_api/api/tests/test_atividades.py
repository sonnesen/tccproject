from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Atividade, Unidade, Curso, Categoria, Instrutor


class AtividadeViewTestCase(TestCase):
    
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Categoria')
        self.instrutor = Instrutor.objects.create(nome='Instrutor', contato='contato@contato.com', resumo='Resumo')
        self.curso = Curso.objects.create(titulo='Curso', categoria=self.categoria, instrutor=self.instrutor)
        self.unidade = Unidade.objects.create(titulo='Unidade', curso=self.curso)
        self.atividade = Atividade.objects.create(titulo='Atividade teste', unidade=self.unidade)
                 
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/atividades/'
        
    def test_api_can_get_all_atividade(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_atividade(self):
        self.data = {
            'titulo': 'Atividade ....',
            'unidade': self.unidade.id
        }
        self.response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_not_create_atividade(self):
        self.client.logout()
        self.data = {
            'titulo': 'Atividade ....',
            'unidade': self.unidade.id
        }                
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_get_atividade(self):
        self.response = self.client.get('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
        
    def test_api_can_not_get_atividade(self):
        self.response = self.client.get('{}{}/'.format(self.url, 9999), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_api_can_update_atividade(self):
        self.data = {
            'titulo': 'Atividade atualizada',
            'unidade': self.unidade.id
        }                
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)       
        
    def test_api_can_not_update_atividade(self):
        self.client.logout()
        self.data = {
            'titulo': 'Atividade atualizada',
            'unidade': self.unidade.id
        }       
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_delete_atividade(self):
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_api_can_not_delete_atividade(self):
        self.client.logout()
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
