from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from alternatives.models import Category


class BaseView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'Alternatives'
        return context


class AlternativeListView(BaseView, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'alternatives/alternative_list.html')


class AlternativeCreateView(SuccessMessageMixin, BaseView, CreateView):
    model = Alternative
    template_name_suffix = '_create'
    fields = '__all__'
    success_url = reverse_lazy('alternatives:alternative_list')
    success_message = 'Alternative %(name)s was created successfully'

    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('alternatives:alternative_create')
        else:
            self.success_url = reverse_lazy('alternatives:alternative_list')
        return CreateView.post(self, request, *args, **kwargs)


class AlternativeDetailView(BaseView, DetailView):
    model = Alternative


class AlternativeUpdateView(SuccessMessageMixin, BaseView, UpdateView):
    model = Alternative
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('alternatives:alternative_list')
    success_message = 'Alternative %(name)s was updated successfully'

    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('alternatives:alternative_create')
        else:
            self.success_url = reverse_lazy('alternatives:alternative_list')
        return UpdateView.post(self, request, *args, **kwargs)


class AlternativeDeleteView(SuccessMessageMixin, BaseView, DeleteView):
    model = Alternative
    success_url = reverse_lazy('alternatives:alternative_list')
    success_message = 'Alternative %(name)s was removed successfully'

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        obj = self.get_object(Alternative.objects.filter(pk=pk))
        messages.success(self.request, self.success_message % obj.__dict__)
        return DeleteView.delete(self, request, *args, **kwargs)

