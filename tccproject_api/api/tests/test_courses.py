from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Course, Category, Instructor


class CourseViewTestCase(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name='Programming')
        self.instructor = Instructor.objects.create(name='John Doo',
                                                    contact='john@doo.com',
                                                    about='Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.')
        
        self.course = Course.objects.create(
            title='Java:First steps',
            category=self.category,
            instructor=self.instructor,
            keywords='java beginner')
        
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/courses/'
        
    def test_api_can_get_all_courses(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_course(self):
        self.data = {
            'title': 'Java: Object Driven Introduction',
            'category': self.category.id,
            'instructor': self.instructor.id,
            'keywords': 'java intermediate',
            'units': {}
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
         
    def test_api_can_not_create_course(self):
        self.client.logout()
        self.data = {
            'title': 'Java: Object Driven Introduction',
            'category': self.category.id,
            'instructor': self.instructor.id,
            'keywords': 'java intermediate',
            'units': {}
        }        
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_get_course(self):
        self.response = self.client.get('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
        
    def test_api_can_not_get_course(self):
        self.response = self.client.get('{}{}/'.format(self.url, 9999), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_api_can_update_course(self):        
        self.data = {
            'title': 'Java: Object Driven Introduction',
            'category': self.category.id,
            'instructor': self.instructor.id,
            'keywords': 'java intermediate object driven',
            'units': {}
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
         
    def test_api_can_not_update_course(self):
        self.client.logout()        
        self.data = {
            'title': 'Java: Object Driven Introduction',
            'category': self.category.id,
            'instructor': self.instructor.id,
            'keywords': 'java intermediate object driven',
            'units': {}
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_delete_course(self):
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_api_can_not_delete_course(self):
        self.client.logout()
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
