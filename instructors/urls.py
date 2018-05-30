from django.urls import path

from instructors.views import (InstructorListView, InstructorCreateView,
                               InstructorDetailView, InstructorUpdateView,
                               InstructorDeleteView)

app_name = 'instructors'

urlpatterns = [
    path('', InstructorListView.as_view(),
         name="instructor_list"),
    path('create/', InstructorCreateView.as_view(),
         name='instructor_create'),
    path('<int:pk>/', InstructorDetailView.as_view(),
         name="instructor_detail"),
    path('<int:pk>/edit/', InstructorUpdateView.as_view(),
         name="instructor_edit"),
    path('<int:pk>/delete/', InstructorDeleteView.as_view(),
         name="instructor_delete")
]
