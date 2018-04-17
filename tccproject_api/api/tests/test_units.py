from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Unit, Course, Category, Instructor


class UnitViewTestCase(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name='Programming')
        self.instructor = Instructor.objects.create(name='John Doo',
                                                    contact='john@doo.com',
                                                    about='Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.')
        
        self.course = Course.objects.create(title='Java:First steps',
                                            category=self.category,
                                            instructor=self.instructor,
                                            keywords='java beginner')
        
        self.unit = Unit.objects.create(title='Description',
                                        course=self.course)
        
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/units/'
        
    def test_api_can_get_all_units(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_unit(self):
        self.data = {
            'title': 'Unit 1',
            'course': self.course.id
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_not_create_unit(self):
        self.client.logout()
        self.data = {
            'title': 'Unit 1',
            'course': self.course.id
        }        
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_get_unit(self):
        self.response = self.client.get('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
        
    def test_api_can_not_get_unit(self):
        self.response = self.client.get('{}{}/'.format(self.url, 9999), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_api_can_update_unit(self):
        self.data = {
            'title': 'Nova Unit 1',
            'course': self.course.id
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)       
        
    def test_api_can_not_update_unit(self):
        self.client.logout()
        self.data = {
            'title': 'Nova Unit 1',
            'course': self.course.id
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_delete_unit(self):
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_api_can_not_delete_unit(self):
        self.client.logout()
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
