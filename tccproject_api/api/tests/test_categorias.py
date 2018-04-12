from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Categoria


class CategoriaViewTestCase(TestCase):
    
    def setUp(self):
        Categoria.objects.create(nome='Mobile')
        
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/categorias/'
        
    def test_api_can_get_all_categoria(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_categoria(self):
        self.data = {'nome': 'Programação'}
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_get_categoria(self):
        self.response = self.client.get(self.url, kwargs={'pk': 1}, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
    
    def test_api_can_update_categoria(self):        
        self.response = self.client.put(
            '{url}{pk}/'.format(url=self.url, pk=1),
            data={'nome': 'Dispositivos Móveis'},
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)       
        
    def test_api_can_delete_categoria(self):
        self.response = self.client.delete('{url}{pk}/'.format(url=self.url, pk=1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)