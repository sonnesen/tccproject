from django.urls.conf import path

from dashboard.views import DashboardView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='home')
]
