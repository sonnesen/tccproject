from django.urls.conf import re_path, include
from rest_framework.routers import DefaultRouter

from api import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'instructors', views.InstructorViewSet)
router.register(r'units', views.UnitViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'resources', views.ResourceViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'alternatives', views.AlternativeViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    re_path(r'^api/v1/', include(router.urls))
]
