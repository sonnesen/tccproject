"""tccproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from activities.api.viewsets import ActivityViewSet
from categories.api.viewsets import CategoryViewSet
from courses.api.viewsets import CourseViewSet
from instructors.api.viewsets import InstructorViewSet
from resources.api.viewsets import ResourceViewSet
from units.api.viewsets import UnitViewSet
from dashboard import urls as dashboard_urls


router = routers.SimpleRouter()
router.register('instructors', InstructorViewSet)
router.register('categories', CategoryViewSet)
router.register('courses', CourseViewSet)
router.register('units', UnitViewSet)
router.register('activities', ActivityViewSet)
router.register('resources', ResourceViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', include(dashboard_urls, namespace='dashboard')),
    path('api-token-auth/', obtain_auth_token),
    path('schema/', schema_view),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
