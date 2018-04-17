from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Question, Unit, Course, Category, Instructor, Alternative, Test


class AlternativeViewTestCase(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name='Category')
        self.instructor = Instructor.objects.create(name='Instructor', contact='contact@contact.com', about='About')
        self.course = Course.objects.create(title='Course', category=self.category, instructor=self.instructor)
        self.unit = Unit.objects.create(title='Unit', course=self.course)
        self.test = Test.objects.create(title='Test', unit=self.unit)
        self.question = Question.objects.create(statement='Question', test=self.test)
        self.alternative = Alternative.objects.create(
            description='Description',
            answer='Answer',
            question=self.question,
            is_correct_answer=False
        )                
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/alternatives/'
        
    def test_api_can_get_all_alternatives(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_alternative(self):
        self.data = {
            'description': 'Description test',
            'answer': 'Answer test',
            'question' : self.question.id,
            'is_correct_answer': False
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_not_create_alternative(self):
        self.client.logout()
        self.data = {
            'description': 'Description test',
            'answer': 'Answer test',
            'question' : self.question.id,
            'is_correct_answer': False
        }        
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_get_alternative(self):
        self.response = self.client.get('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)    
        
    def test_api_can_not_get_alternative(self):
        self.response = self.client.get('{}{}/'.format(self.url, 9999), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_api_can_update_alternative(self):
        self.data = {
            'description': 'Description test ...',
            'answer': 'Answer test ...',
            'question' : self.question.id,
            'is_correct_answer': True
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)       
        
    def test_api_can_not_update_alternative(self):
        self.client.logout()
        self.data = {
            'description': 'Description test ...',
            'answer': 'Answer test ...',
            'question' : self.question.id,
            'is_correct_answer': True
        }        
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_api_can_delete_alternative(self):
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_api_can_not_delete_alternative(self):
        self.client.logout()
        self.response = self.client.delete('{}{}/'.format(self.url, 1), format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
