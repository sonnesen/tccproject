from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.base import View

from accounts.forms import RegistrationForm


class RegistrationView(View):
    template_name = 'registration/register.html'
    
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
            return redirect('dashboard:principal')
        else:
            context = { 'form': form }
            return render(request, self.template_name, context)
