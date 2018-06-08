from django.urls import path

from alternatives.views import (AlternativeListView, AlternativeCreateView,
                                AlternativeDetailView, AlternativeUpdateView,
                                AlternativeDeleteView)

app_name = 'alternatives'

urlpatterns = [
    path('', AlternativeListView.as_view(),
         name="alternative_list"),
    path('create/', AlternativeCreateView.as_view(),
         name='alternative_create'),
    path('<int:pk>/', AlternativeDetailView.as_view(),
         name="alternative_detail"),
    path('<int:pk>/edit/', AlternativeUpdateView.as_view(),
         name="alternative_edit"),
    path('<int:pk>/delete/', AlternativeDeleteView.as_view(),
         name="alternative_delete")
]
