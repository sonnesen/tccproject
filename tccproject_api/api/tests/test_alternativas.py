from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Alternativa


class AlternativaViewTestCase(TestCase):
    
    def setUp(self):
        self.alternativa = Alternativa.objects.create(descricao='Descrição',
                                                      justificativa='Justificativa',
                                                      questao=None,
                                                      correta=False)
        
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/alternativas/'
        
    def test_api_can_get_all_alternativa(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_alternativa(self):
        self.data = {
            'descricao': 'Descrição',
            'justificativa': 'justificativa',
            'questao': {},
            'correta': False
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_not_create_alternativa(self):
        self.client.logout()
        self.data = {
            'descricao': 'Descrição',
            'justificativa': 'justificativa',
            'questao': {},
            'correta': False
        }        
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_get_alternativa(self):
        self.response = self.client.get('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
        
    def test_api_can_not_get_alternativa(self):
        self.response = self.client.get('{}{}/'.format(self.url, 9999), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_api_can_update_alternativa(self):
        self.data = {
            'descricao': 'Nova descrição',
            'justificativa': 'Nova justificativa',
            'questao': {},
            'correta': True
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)       
        
    def test_api_can_not_update_alternativa(self):
        self.client.logout()
        self.data = {
            'descricao': 'Nova descrição',
            'justificativa': 'Nova justificativa',
            'questao': {},
            'correta': True
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_delete_alternativa(self):
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_api_can_not_delete_alternativa(self):
        self.client.logout()
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
