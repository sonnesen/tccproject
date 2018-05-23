from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from activities.api.viewsets import ActivityViewSet
from categories.api.viewsets import CategoryViewSet
from courses import urls as courses_urls
from courses.api.viewsets import CourseViewSet
from dashboard import urls as dashboard_urls
from instructors.api.viewsets import InstructorViewSet
from resources.api.viewsets import ResourceViewSet
from units.api.viewsets import UnitViewSet


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
    path('courses/', include(courses_urls, namespace='courses')),
    path('api-token-auth/', obtain_auth_token),
    path('schema/', schema_view),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
