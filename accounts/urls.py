from django.contrib.auth import views as auth_views
from django.urls.conf import path

from accounts import views as accounts_views

app_name = 'accounts'

urlpatterns = [
#     path('', accounts_views.dashboard, name='dashboard'),
    path('entrar/', auth_views.login,
         {'template_name': 'accounts/register/login.html'}, name='login'),
    path('sair/', auth_views.logout,
         {'next_page': 'core:home'}, name='logout'),
#     path('cadastre-se/', accounts_views.register, name='register'),
#     path('nova-senha/', accounts_views.password_reset, name='password_reset'),
#     path('confirmar-nova-senha/<key>/', accounts_views.password_reset_confirm,
#          name='password_reset_confirm'), path('editar/', accounts_views.edit, name='edit'),
#     path('editar-senha/', accounts_views.edit_password, name='edit_password'),
]
