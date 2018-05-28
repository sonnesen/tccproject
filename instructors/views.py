from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.base import View
from django.urls import reverse_lazy

from instructors.models import Instructor


class BaseView(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'Instructors'
        return context


class InstructorListView(BaseView, ListView):
    paginate_by = 10
    model = Instructor


class InstructorDetailView(BaseView, DetailView):
    model = Instructor


class InstructorUpdateView(BaseView, UpdateView):
    model = Instructor
    fields = ['name', 'contact', 'about']
    template_name_suffix = '_update'
    success_url = reverse_lazy('instructors:instructor_list')


class InstructorDeleteView(BaseView, DeleteView):
    pass
