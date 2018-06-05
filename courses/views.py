from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models.functions.base import Lower
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courses.models import Course
from taggit.models import Tag


class BaseView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(kwargs)
        context['current_page'] = 'Courses'
        return context


class CourseListView(BaseView, View):

    def get_context_data(self, **kwargs):
#         context = super().get_context_data(kwargs)        
        return BaseView.get_context_data(self, **kwargs)
    
    def get(self, request, *args, **kwargs):
        if request.GET.get('type') == 'json':
            draw_page = int(request.GET.get('draw'))
            registers_per_page = int(request.GET.get('length'))
            first_record_in_page = int(request.GET.get('start'))
            page = int(first_record_in_page / registers_per_page) + 1
            error = ''

            queryset = Course.objects.all()
            recordsTotal = queryset.count()
            recordsFiltered = recordsTotal

            search_value = request.GET.get('search[value]')
            if search_value:
                queryset = queryset.filter(
                    Q(name__icontains=search_value) |
                    Q(category__icontains=search_value) |
                    Q(instructor__icontains=search_value)
                )
                recordsFiltered = queryset.count()

            if request.GET.get('order[0][column]') == '2':
                query_order_by = 'category'
            elif request.GET.get('order[0][column]') == '3':
                query_order_by = 'instructor'
            else:
                query_order_by = 'name'

            if request.GET.get('order[0][dir]') == 'desc':
                queryset = queryset.order_by(Lower(query_order_by).desc())
            else:
                queryset = queryset.order_by(Lower(query_order_by))

            paginator = Paginator(queryset, registers_per_page)
            courses_page = paginator.get_page(page)
            courses_list = list(courses_page.object_list.values())
            
            for course in courses_list:
                course = Course(**course)
                course.keywords = Tag.objects.filter(object_id=course.id)

            json = {
                'draw': draw_page,
                'recordsTotal': recordsTotal,
                'recordsFiltered': recordsFiltered,
                'data': courses_list,
                'error': error
            }

            return JsonResponse(json)
        else:
            return render(request, 'courses/course_list.html')


class CourseCreateView(SuccessMessageMixin, BaseView, CreateView):
    model = Course
    template_name_suffix = '_create'
    fields = '__all__'
    success_url = reverse_lazy('courses:course_list')
    success_message = 'Course %(name)s was created successfully'

    def post(self, request, *args, **kwargs):
        if request.POST.get('saveandnew'):
            self.success_url = reverse_lazy('courses:course_create')
        else:
            self.success_url = reverse_lazy('courses:course_list')
        return CreateView.post(self, request, *args, **kwargs)


class CourseDetailView(BaseView, DetailView):
    model = Course


class CourseUpdateView(SuccessMessageMixin, BaseView, UpdateView):
    model = Course
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('courses:course_list')
    success_message = 'Course %(name)s was updated successfully'

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

