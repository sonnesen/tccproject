from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import path

from accounts.views import RegistrationView, UserUpdateView, \
    UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
#     path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

#     path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('register/', RegistrationView.as_view(), name='register'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change')
]
