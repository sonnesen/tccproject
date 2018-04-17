from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Instructor


class InstructorViewTestCase(TestCase):
    
    def setUp(self):
        Instructor.objects.create(name='John Doo',
                                  contact='john@doo.com',
                                  about='Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.')
        
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/instructors/'
        
    def test_api_can_get_all_instructors(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_instructor(self):
        self.data = {
            'name': 'Siclano da Silva',
            'contact': 'siclano@test.com',
            'about': 'Vis te quas soluta, no augue tollit vel.'
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_not_create_instructor(self):
        self.client.logout()
        self.data = {
            'name': 'Siclano da Silva',
            'contact': 'siclano@test.com',
            'about': 'Vis te quas soluta, no augue tollit vel.'
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_get_instructor(self):
        self.response = self.client.get('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
        
    def test_api_can_not_get_instructor(self):
        self.response = self.client.get('{}{}/'.format(self.url, 9999), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_api_can_update_instructor(self):
        self.data = {
            'name': 'John Doo',
            'contact': 'fulano@gmail.com',
            'about': 'Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.'
        }
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)       
        
    def test_api_can_not_update_instructor(self):
        self.client.logout()
        self.data = {
            'name': 'John Doo',
            'contact': 'fulano@gmail.com',
            'about': 'Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.'
        }
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_delete_instructor(self):
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_api_can_not_delete_instructor(self):
        self.client.logout()
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
