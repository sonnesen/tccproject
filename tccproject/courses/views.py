from django.views.generic.list import ListView
from courses.models import Course
from django.views.generic.detail import DetailView


class CourseListView(ListView):
    paginate_by = 10
    model = Course
    template_name = 'courses/list.html'
    context_object_name = 'courses'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Courses'
        return context
    
class CourseDetailView(DetailView):
    pass    
    