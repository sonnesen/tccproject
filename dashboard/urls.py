from django.urls.conf import path

from dashboard.views import DashboardView

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
