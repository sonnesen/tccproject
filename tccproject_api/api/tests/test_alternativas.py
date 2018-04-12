from django.contrib.auth.models import User
from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Alternativa, Questao, Avaliacao, Unidade, Curso,\
    Categoria, Instrutor


class AlternativaViewTestCase(TestCase):
    
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
        
        self.unidade = Unidade.objects.create(titulo='unidade', curso=self.curso)
        self.avaliacao = Avaliacao.objects.create(unidade=self.unidade)
        self.questao = Questao.objects.create(enunciado='Enunciado', avaliacao=self.avaliacao)
        self.alternativa = Alternativa.objects.create(descricao='Descrição',
                                                      justificativa='Justificativa',
                                                      questao=self.questao,
                                                      correta=False)
        
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin@123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/v1/alternativaes/'
        
    def test_api_can_get_all_alternativa(self):
        self.response = self.client.get(self.url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_api_can_create_alternativa(self):
        self.data = {
            'nome': 'Siclano da Silva',
            'contato': 'siclano@test.com',
            'resumo': 'Vis te quas soluta, no augue tollit vel.'
        }
        self.response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_not_create_alternativa(self):
        self.client.logout()
        self.data = {
            'nome': 'Siclano da Silva',
            'contato': 'siclano@test.com',
            'resumo': 'Vis te quas soluta, no augue tollit vel.'
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
            'nome': 'Fulano de Tal',
            'contato': 'fulano@gmail.com',
            'resumo': 'Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.'
        }
        self.response = self.client.put(
            '{}{}/'.format(self.url, 1),
            data=self.data,
            format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)       
        
    def test_api_can_not_update_alternativa(self):
        self.client.logout()
        self.data = {
            'nome': 'Fulano de Tal',
            'contato': 'fulano@gmail.com',
            'resumo': 'Lorem ipsum dolor sit amet, te quo illum iuvaret corpora.'
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
