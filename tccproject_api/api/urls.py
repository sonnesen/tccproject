from django.urls.conf import re_path, include
from rest_framework.routers import DefaultRouter

from api import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cursos', views.CursoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'instrutores', views.InstrutorViewSet)
router.register(r'unidades', views.UnidadeViewSet)
router.register(r'atividades', views.AtividadeViewSet)
# router.register(r'videos', views.VideoAulaViewSet)
# router.register(r'materiais', views.MaterialComplementarViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    re_path(r'^api/v1/', include(router.urls))
]
