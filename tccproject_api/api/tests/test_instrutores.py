from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Instrutor


class InstrutorViewTestCase(TestCase):
    
    def setUp(self):
        Instrutor.objects.create(nome='Fulano de Tal',
                                 contato='fulano@test.com',
                                 resumo='Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.')
        
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/instrutores/'
        
    def test_api_can_get_all_instrutor(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_instrutor(self):
        self.data = {
            'nome': 'Siclano da Silva',
            'contato': 'siclano@test.com',
            'resumo': 'Vis te quas soluta, no augue tollit vel.'
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_get_instrutor(self):
        self.response = self.client.get(self.url, kwargs={'pk': 1}, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
    
    def test_api_can_update_instrutor(self):
        self.response = self.client.put(
            '{url}{pk}/'.format(url=self.url, pk=1),
            data={
            'nome': 'Fulano de Tal',
            'contato': 'fulano@gmail.com',
            'resumo': 'Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.'
        },
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)       
        
    def test_api_can_delete_instrutor(self):
        self.response = self.client.delete('{url}{pk}/'.format(url=self.url, pk=1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
