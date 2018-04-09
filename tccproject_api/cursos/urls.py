from rest_framework.routers import DefaultRouter
from cursos import views
from django.urls.conf import re_path, include

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cursos', views.CursoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'instrutores', views.InstrutorViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    re_path(r'^', include(router.urls))
]
