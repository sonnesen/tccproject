from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from categories.models import Category


class BaseView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'Categories'
        return context


class CategoryListView(BaseView, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'categories/category_list.html')


class CategoryCreateView(SuccessMessageMixin, BaseView, CreateView):
    model = Category
    template_name_suffix = '_create'
    fields = '__all__'
    success_url = reverse_lazy('categories:category_list')
    success_message = 'Category %(name)s was created successfully'

    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('categories:category_create')
        else:
            self.success_url = reverse_lazy('categories:category_list')
        return CreateView.post(self, request, *args, **kwargs)


class CategoryDetailView(BaseView, DetailView):
    model = Category


class CategoryUpdateView(SuccessMessageMixin, BaseView, UpdateView):
    model = Category
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('categories:category_list')
    success_message = 'Category %(name)s was updated successfully'

    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('categories:category_create')
        else:
            self.success_url = reverse_lazy('categories:category_list')
        return UpdateView.post(self, request, *args, **kwargs)


class CategoryDeleteView(SuccessMessageMixin, BaseView, DeleteView):
    model = Category
    success_url = reverse_lazy('categories:category_list')
    success_message = 'Category %(name)s was removed successfully'

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        obj = self.get_object(Category.objects.filter(pk=pk))
        messages.success(self.request, self.success_message % obj.__dict__)
        return DeleteView.delete(self, request, *args, **kwargs)

