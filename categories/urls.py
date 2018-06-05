from django.urls import path

from categories.views import (CategoryListView, CategoryCreateView,
                              CategoryDetailView, CategoryUpdateView,
                              CategoryDeleteView)

app_name = 'categories'

urlpatterns = [
    path('', CategoryListView.as_view(),
         name="category_list"),
    path('create/', CategoryCreateView.as_view(),
         name='category_create'),
    path('<int:pk>/', CategoryDetailView.as_view(),
         name="category_detail"),
    path('<int:pk>/edit/', CategoryUpdateView.as_view(),
         name="category_edit"),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(),
         name="category_delete")
]
