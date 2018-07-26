from django.urls.conf import path

from principal.views import HomeView

app_name = 'principal'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
