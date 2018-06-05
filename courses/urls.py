from django.urls import path

from courses.views import (CourseListView, CourseCreateView,
                           CourseDetailView, CourseUpdateView,
                           CourseDeleteView)

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(),
         name="course_list"),
    path('create/', CourseCreateView.as_view(),
         name='course_create'),
    path('<int:pk>/', CourseDetailView.as_view(),
         name="course_detail"),
    path('<int:pk>/edit/', CourseUpdateView.as_view(),
         name="course_edit"),
    path('<int:pk>/delete/', CourseDeleteView.as_view(),
         name="course_delete")
]
