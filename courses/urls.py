from django.urls import path

from courses.views import CourseListView, CourseDetailView, EnrollmentView, \
    HomeView, DashboardView, UnitListView, UnitDetailView, UnitVideoView, \
    ExamDetailView, ExamFormView


app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:course_id>/detail/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/<int:course_id>/enrollment/', EnrollmentView.as_view(), name='enrollment'),
    path('courses/<int:course_id>/units/', UnitListView.as_view(), name='course_units'),
    path('courses/<int:course_id>/units/<int:unit_id>/', UnitDetailView.as_view(), name='unit_detail'),
    path('courses/<int:course_id>/units/<int:unit_id>/video/<int:video_id>/', UnitVideoView.as_view(), name='unit_video'),
    path('courses/<int:course_id>/units/<int:unit_id>/exam/<int:exam_id>/detail/', ExamDetailView.as_view(), name='exam_detail'),
    path('courses/<int:course_id>/units/<int:unit_id>/exam/<int:exam_id>/form/', ExamFormView.as_view(), name='exam_form'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
#     path('', InstructorListView.as_view(), name="instructor_list"),
#     path('create/', InstructorCreateView.as_view(), name='instructor_create'),
#     path('<int:pk>/', InstructorDetailView.as_view(), name="instructor_detail"),
#     path('<int:pk>/edit/', InstructorUpdateView.as_view(), name="instructor_edit"),
#     path('<int:pk>/delete/', InstructorDeleteView.as_view(), name="instructor_delete") 

#     path('', AlternativeListView.as_view(), name="alternative_list"),
#     path('create/', AlternativeCreateView.as_view(), name='alternative_create'),
#     path('<int:pk>/', AlternativeDetailView.as_view(), name="alternative_detail"),
#     path('<int:pk>/edit/', AlternativeUpdateView.as_view(), name="alternative_edit"),
#     path('<int:pk>/delete/', AlternativeDeleteView.as_view(), name="alternative_delete")  

#     path('', CategoryListView.as_view(), name="category_list"),
#     path('create/', CategoryCreateView.as_view(), name='category_create'),
#     path('<int:pk>/', CategoryDetailView.as_view(), name="category_detail"),
#     path('<int:pk>/edit/', CategoryUpdateView.as_view(), name="category_edit"),
#     path('<int:pk>/delete/', CategoryDeleteView.as_view(), name="category_delete")

]
