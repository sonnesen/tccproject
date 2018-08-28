from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm
from django.forms.fields import CharField
from django.forms.models import ModelForm
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
    
    first_name = CharField(label='Nome', required=True, max_length=30)
    last_name = CharField(label='Sobrenome', required=True, max_length=150)
    email = CharField(label='E-mail',required=True, max_length=254)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }

        
class MyUserChangeForm(ModelForm):    
    
    first_name = CharField(label='Nome', required=True, max_length=30)
    last_name = CharField(label='Sobrenome', required=True, max_length=150)
    email = CharField(label='E-mail', required=True, max_length=254)
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }
             
