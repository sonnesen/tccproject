from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.forms.forms import Form
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView

# from courses.forms import ExamForm
from courses.models import Course, Enrollment, Unit, Video, Document, Exam, \
    ExamTry, WatchedVideos, Answer


class CourseListView(View):

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        context = { 'courses': courses }
        return render(request, 'courses/course_list.html', context)


class CourseDetailView(DetailView):
    model = Course
    pk_url_kwarg = 'course_id'


class EnrollmentView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        return self.post(request, args, kwargs)
        
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs.get('course_id'))
        user = request.user
        
        (enrollment, is_created) = Enrollment.objects.get_or_create(user=user, course=course)
        
        if is_created:
            messages.success(request, 'Inscrição no curso {} efetuada com sucesso!'.format(course))
        else:
            messages.warning(request, 'Usuário já inscrito no curso {}!'.format(course))
        
        return redirect('courses:dashboard')


class DashboardView(View):
    template_name = 'dashboard/dashboard.html'
    context = {}
    
    def get(self, request):
        return render(request, self.template_name, self.context)  

    
class HomeView(View):
    template_name = 'home/home.html'
    context = {}
    
    def get(self, request):
        return render(request, self.template_name, self.context)

    
class UnitListView(LoginRequiredMixin, View):
    template_name = 'units/units_list.html'
    context = {}
    
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs.get('course_id'))
        self.context = {
            'course': course
        }
        return render(request, self.template_name, self.context)

    
class UnitDetailView(LoginRequiredMixin, View):
    template_name = 'units/unit_detail.html'
    context = {}
    
    def get(self, request, *args, **kwargs):        
        course = get_object_or_404(Course, pk=kwargs.get('course_id'))
        unit = get_object_or_404(Unit, pk=kwargs.get('unit_id'))
        
        self.context = {
            'course': course,
            'unit': unit
        }
        
        return render(request, self.template_name, self.context)    

    
class UnitVideoView(LoginRequiredMixin, View):
    template_name = 'units/unit_video.html'
    context = {}
    
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs.get('course_id'))
        unit = get_object_or_404(Unit, pk=kwargs.get('unit_id'))
        video = get_object_or_404(Video, pk=kwargs.get('video_id'))
        
        self.context = {
            'course': course,
            'unit': unit,
            'video': video
        }
        
        watched_videos, created = WatchedVideos.objects.get_or_create(user=request.user, video=video)
        watched_videos.times = watched_videos.times + 1
        watched_videos.save()
        
        return render(request, self.template_name, self.context)

    
class UnitDocumentView(LoginRequiredMixin, View):
    template_name = 'units/unit_document.html'
    context = {}
    
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs.get('course_id'))
        unit = get_object_or_404(Unit, pk=kwargs.get('unit_id'))
        document = get_object_or_404(Document, pk=kwargs.get('document_id'))
        
        self.context = {
            'course': course,
            'unit': unit,
            'document': document
        }
        
        return render(request, self.template_name, self.context)   

    
class ExamDetailView(LoginRequiredMixin, View):
    template_name = 'exams/exam_detail.html'
    context = {}
    
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs.get('course_id'))
        unit = get_object_or_404(Unit, pk=kwargs.get('unit_id'))
        exam = get_object_or_404(Exam, pk=kwargs.get('exam_id'))
        tries = ExamTry.objects.filter(user=request.user, exam=exam).all()        
        
        self.context = {
            'course': course,
            'unit': unit,
            'exam': exam,
            'tries': tries,
        }
        
        return render(request, self.template_name, self.context)

    
class ExamFormView(LoginRequiredMixin, View):
    template_name = 'exams/exam_form.html'
    context = {}
    
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs.get('course_id'))
        unit = get_object_or_404(Unit, pk=kwargs.get('unit_id'))
        exam = get_object_or_404(Exam, pk=kwargs.get('exam_id'))        
        
        self.context = {
            'course': course,
            'unit': unit,
            'exam': exam,
            'form': {'fields': []}
        }
        
        for question in exam.questions.all():
            question_tag_name = 'question_{}'.format(question.pk)
            self.context['form']['fields'].append({'name': question_tag_name})                
        
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs.get('course_id'))
        unit = get_object_or_404(Unit, pk=kwargs.get('unit_id'))
        exam = get_object_or_404(Exam, pk=kwargs.get('exam_id'))
        
        self.context = {
            'course': course,
            'unit': unit,
            'exam': exam,
            'form': {'fields': []}
        }
        
        has_error = False
        user_answers = list()
        questions = exam.questions.all()
        
        for question in questions:
            question_tag_name = 'question_{}'.format(question.pk)
            user_answer = request.POST.get(question_tag_name)
            
            if not user_answer:
                has_error = True
                self.context['form']['fields'].append(
                    {
                        'name': question_tag_name,
                        'errors': ['Você não respondeu esta pergunta!']
                    })
            else:
                user_answers.append(
                    {
                        'question_id':question.pk,
                        'question_tag_name':question_tag_name,
                        'alternative_id':int(user_answer)
                    })
        
        self.context['user_answers'] = user_answers
                 
        if has_error:
            return render(request, self.template_name, self.context)
        
        exam_try = ExamTry(exam=exam, user=request.user)
        hits = 0
        answers = list()
        
        for user_answer in user_answers:
            for question in questions:
                if question.pk == user_answer['question_id']:
                    for alternative in question.alternatives.all():                        
                        if alternative.pk == user_answer['alternative_id']:                            
                            answer = Answer(exam_try=exam_try, alternative=alternative)
                            if alternative.is_correct:
                                answer.hit_the_answer = True
                                hits = hits + 1
                            answers.append(answer)                            
                            break               
                            
        exam_try.hits = hits
        exam_try.save()
        
        for answer in answers:
            answer.exam_try = exam_try
            answer.save()
        
        return redirect ('courses:exam_detail', course_id=1, unit_id=1, exam_id=1)
        
