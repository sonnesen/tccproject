from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from accounts import urls as accounts_urls
from courses import urls as courses_urls
from courses.api.viewsets import CourseViewSet, DocumentViewSet, VideoViewSet, \
    InstructorViewSet, CategoryViewSet, UnitViewSet, AlternativeViewSet, \
    ExamViewSet, QuestionViewSet

# from django.contrib.auth import urls as auth_urls
router = routers.SimpleRouter()

router.register('categories', CategoryViewSet)
router.register('instructors', InstructorViewSet)
router.register('courses', CourseViewSet)
router.register('units', UnitViewSet)
# router.register('enrollments', EnrollmentViewSet)
router.register('documents', DocumentViewSet)
router.register('videos', VideoViewSet)
router.register('exams', ExamViewSet)
router.register('questions', QuestionViewSet)
router.register('alternatives', AlternativeViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', include(courses_urls, namespace='courses')),
    path('api-token-auth/', obtain_auth_token),
    path('schema/', schema_view),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
