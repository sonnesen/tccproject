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

from instructors.models import Instructor


class BaseView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'Instructors'
        return context


class InstructorListView(BaseView, View):

    def get(self, request, *args, **kwargs):
        if request.GET.get('type') == 'json':
            draw_page = int(request.GET.get('draw'))
            registers_per_page = int(request.GET.get('length'))
            first_record_in_page = int(request.GET.get('start'))
            page = int(first_record_in_page / registers_per_page) + 1
            error = ''

            queryset = Instructor.objects.all()
            recordsTotal = queryset.count()
            recordsFiltered = recordsTotal

            search_value = request.GET.get('search[value]')
            if search_value:
                queryset = queryset.filter(
                    Q(name__icontains=search_value) |
                    Q(contact__icontains=search_value)
                )
                recordsFiltered = queryset.count()

            if request.GET.get('order[0][column]') == '1':
                query_order_by = 'contact'
            elif request.GET.get('order[0][column]') == '2':
                query_order_by = 'about'
            else:
                query_order_by = 'name'

            if request.GET.get('order[0][dir]') == 'desc':
                queryset = queryset.order_by(Lower(query_order_by).desc())
            else:
                queryset = queryset.order_by(Lower(query_order_by))

            paginator = Paginator(queryset, registers_per_page)
            instructors_page = paginator.get_page(page)
            instructors_list = list(instructors_page.object_list.values())

            json = {
                'draw': draw_page,
                'recordsTotal': recordsTotal,
                'recordsFiltered': recordsFiltered,
                'data': instructors_list,
                'error': error
            }

            return JsonResponse(json)
        else:
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
    fields = '__all__' #['name', 'contact', 'about']
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

