from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import UpdateView

from accounts.forms import RegistrationForm, MyUserChangeForm


class RegistrationView(View):
    template_name = 'accounts/register.html'
    
    def get(self, request):
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('courses:home')
        else:
            context = { 'form': form }
            return render(request, self.template_name, context)


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = MyUserChangeForm
    template_name = 'accounts/user_update_form.html'
    success_message = 'Dados do usuário atualizados com sucesso!'
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse('courses:dashboard')
    
class UserPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('courses:dashboard')
    success_message = 'Senha atualizada com sucesso!' 
    
