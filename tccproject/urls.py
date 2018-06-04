from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from categories.api.viewsets import CategoryViewSet
from courses import urls as courses_urls
from instructors import urls as instructors_urls
from categories import urls as categories_urls
from courses.api.viewsets import CourseViewSet
from dashboard import urls as dashboard_urls
from documents.api.viewsets import DocumentViewSet
from instructors.api.viewsets import InstructorViewSet
from units.api.viewsets import UnitViewSet
from videos.api.viewsets import VideoViewSet

router = routers.SimpleRouter()
router.register('instructors', InstructorViewSet)
router.register('categories', CategoryViewSet)
router.register('courses', CourseViewSet)
router.register('units', UnitViewSet)
router.register('videos', VideoViewSet)
router.register('documents', DocumentViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', include(dashboard_urls, namespace='dashboard')),
    path('api-token-auth/', obtain_auth_token),
    path('schema/', schema_view),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('courses/', include(courses_urls, namespace='courses')),
    path('instructors/', include(instructors_urls, namespace='instructores')),
    path('categories/', include(categories_urls, namespace='categories')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
