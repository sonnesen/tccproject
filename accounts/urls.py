from django.contrib.auth.views import LoginView
from django.urls.conf import path

from accounts.views import RegisterView


app_name = 'accounts'

urlpatterns = [
#     path('', accounts_views.dashboard, name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
#    path('sair/', auth_views.logout, {'next_page': 'core:home'}, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
#     path('nova-senha/', accounts_views.password_reset, name='password_reset'),
#     path('confirmar-nova-senha/<key>/', accounts_views.password_reset_confirm,
#          name='password_reset_confirm'), path('editar/', accounts_views.edit, name='edit'),
#     path('editar-senha/', accounts_views.edit_password, name='edit_password'),
]
