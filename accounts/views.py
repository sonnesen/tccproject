from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.base import View

from accounts.forms import RegisterForm

User = get_user_model


class RegisterView(View):
    template_name = 'registration/register.html'
    
    def get(self, request):
        context = { 'form': RegisterForm() }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('dashboard:index')
 
# def password_reset(request):
#     template_name = 'accounts/password_reset.html'
#     context = {}
#     form = PasswordResetForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         context['success'] = True
#     context['form'] = form
#     return render(request, template_name, context)
# 
# 
# def password_reset_confirm(request, key):
#     template_name = 'accounts/password_reset_confirm.html'
#     context = {}
#     reset = get_object_or_404(PasswordReset, key=key)
#     form = SetPasswordForm(user=reset.user, data=request.POST or None)
#     if form.is_valid():
#         form.save()
#         context['success'] = True
#     context['form'] = form
#     return render(request, template_name, context)
# 
# 
# @login_required
# def edit(request):
#     template_name = 'accounts/edit.html'
#     context = {}
#     if request.method == 'POST':
#         form = EditAccountForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, 'Os dados da sua conta foram alterados com sucesso'
#             )
#             return redirect('accounts:dashboard')
#     else:
#         form = EditAccountForm(instance=request.user)
#     context['form'] = form
#     return render(request, template_name, context)
# 
# 
# @login_required
# def edit_password(request):
#     template_name = 'accounts/edit_password.html'
#     context = {}
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             context['success'] = True
#     else:
#         form = PasswordChangeForm(user=request.user)
#     context['form'] = form
#     return render(request, template_name, context)
