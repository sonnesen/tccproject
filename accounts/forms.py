from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput, TextInput, EmailInput
from django.utils.translation import gettext_lazy as _


class MyAuthenticationForm(AuthenticationForm):
    
    username = UsernameField(
        max_length=254,
        widget=TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    
    password = CharField(
        label=_("Password"),
        strip=False,
        widget=PasswordInput({'class': 'form-control'}),
    )
    

class RegistrationForm(UserCreationForm):
    
    email = CharField(max_length=254, required=True, widget=EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        } 
