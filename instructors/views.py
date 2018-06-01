from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from django.urls import reverse_lazy

from instructors.models import Instructor
from django.contrib.messages.views import SuccessMessageMixin


class BaseView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'Instructors'
        return context


class InstructorListView(BaseView, ListView):
#     paginate_by = 10
    model = Instructor


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
    fields = ['name', 'contact', 'about']
    template_name_suffix = '_update'
    success_url = reverse_lazy('instructors:instructor_list')
    success_message = 'Instructor %(name)s was updated successfully'

    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('instructors:instructor_create')
        else:
            self.success_url = reverse_lazy('instructors:instructor_list') 
        return UpdateView.post(self, request, *args, **kwargs)


class InstructorDeleteView(BaseView, DeleteView):
    model = Instructor
    success_url = reverse_lazy('instructors:instructor_list')
