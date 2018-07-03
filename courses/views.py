from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.forms.models import ModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from categories.models import Category
from courses.models import Course
from instructors.models import Instructor


class BaseView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'Courses'
        return context


class CourseListView(BaseView, View):

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        context = {
            'courses': courses
        }
        return render(request, 'courses/course_list.html', context)


class CourseCreateView(SuccessMessageMixin, BaseView, CreateView):
    model = Course
    template_name_suffix = '_create'
    fields = '__all__'
    success_url = reverse_lazy('courses:course_list')
    success_message = 'Course %(name)s was created successfully'

    def get(self, request):
        categories = Category.objects.all()
        instructors = Instructor.objects.all()
        context = {
            'categories': categories,
            'instructors': instructors
        }
        return render(request, 'courses/course_create.html', context)
        
    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('courses:course_create')
        else:
            self.success_url = reverse_lazy('courses:course_list')
        return CreateView.post(self, request, *args, **kwargs)


class CourseDetailView(BaseView, DetailView):
    model = Course


class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'category', 'instructor', 'keywords', 
                  'description', 'image']
                
    def keywords_list(self):
        tagfields = self.instance.keywords.all()
        keywords_list = ', '.join(t.name for t in tagfields)
        return keywords_list
        

class CourseUpdateView(SuccessMessageMixin, BaseView, UpdateView):
    model = Course
    template_name_suffix = '_update'
    success_url = reverse_lazy('courses:course_list')
    success_message = 'Course %(name)s was updated successfully'
    form_class = CourseForm    

    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('courses:course_create')
        else:
            self.success_url = reverse_lazy('courses:course_list')
        return UpdateView.post(self, request, *args, **kwargs)


class CourseDeleteView(SuccessMessageMixin, BaseView, DeleteView):
    model = Course
    success_url = reverse_lazy('courses:course_list')
    success_message = 'Course %(name)s was removed successfully'

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        obj = self.get_object(Course.objects.filter(pk=pk))
        messages.success(self.request, self.success_message % obj.__dict__)
        return DeleteView.delete(self, request, *args, **kwargs)

