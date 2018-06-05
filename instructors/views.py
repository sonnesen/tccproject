from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from instructors.models import Instructor


class BaseView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'Instructors'
        return context


class InstructorListView(BaseView, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'instructors/instructor_list.html')


class InstructorCreateView(SuccessMessageMixin, BaseView, CreateView):
    model = Instructor
    template_name_suffix = '_create'
    fields = '__all__'
    success_url = reverse_lazy('instructors:instructor_list')
    success_message = 'Instructor %(name)s was created successfully'

    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('instructors:instructor_create')
        else:
            self.success_url = reverse_lazy('instructors:instructor_list')
        return CreateView.post(self, request, *args, **kwargs)


class InstructorDetailView(BaseView, DetailView):
    model = Instructor


class InstructorUpdateView(SuccessMessageMixin, BaseView, UpdateView):
    model = Instructor
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('instructors:instructor_list')
    success_message = 'Instructor %(name)s was updated successfully'

    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('instructors:instructor_create')
        else:
            self.success_url = reverse_lazy('instructors:instructor_list')
        return UpdateView.post(self, request, *args, **kwargs)


class InstructorDeleteView(SuccessMessageMixin, BaseView, DeleteView):
    model = Instructor
    success_url = reverse_lazy('instructors:instructor_list')
    success_message = 'Instructor %(name)s was removed successfully'

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        obj = self.get_object(Instructor.objects.filter(pk=pk))
        messages.success(self.request, self.success_message % obj.__dict__)
        return DeleteView.delete(self, request, *args, **kwargs)

