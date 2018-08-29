from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.aggregates import Max
from django.utils.text import slugify
from taggit.managers import TaggableManager

from courses.validators import FileValidator


def upload_to_dir(instance, filename):
    if type(instance)._meta.model_name == 'document':
        course_name = slugify(instance.unit.course.name)
        unit_name = slugify(instance.unit.name) 
        return 'docs/{0}/{1}/{2}'.format(course_name, unit_name, filename)
    elif type(instance)._meta.model_name == 'video':
        course_name = slugify(instance.unit.course.name)
        unit_name = slugify(instance.unit.name)
        return 'videos/{0}/{1}/{2}'.format(course_name, unit_name, filename)
    else:
        course_name = slugify(instance.name) 
        return 'images/{0}/{1}'.format(course_name, filename)


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Instructor(models.Model):
    name = models.CharField(max_length=100, null=False)
    contact = models.EmailField(max_length=100, null=False)
    about = models.TextField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,
                                 related_name='categories',
                                 on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor,
                                   related_name='instructors',
                                   on_delete=models.SET_NULL,
                                   blank=True,
                                   null=True)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to=upload_to_dir, null=True, blank=True)
    keywords = TaggableManager('keywords')

    def keywords_list(self):
        return ', '.join(t.name for t in self.keywords.all())

    def __str__(self):
        return self.name
    
    def num_videos(self):
        total = 0
        units = self.units.all()        
        for unit in units:
            total = total + unit.num_videos()
        return total
    
    def videos_list(self):
        videos = list()
        
        for unit in self.units.all():
            for video in unit.videos.all():
                videos.append(video)
                
        return videos
    
    def num_watched_videos_by_user(self, user):
        course_videos = self.videos_list()
        watched_videos = WatchedVideos.objects.filter(user=user, video__in=course_videos).count()
        return watched_videos
    
    def exams_by_user(self, user):
        exams = list()
        units = self.units.all()
        course_exams = list()
        
        for unit in units:
            for exam in unit.exams.all():
                course_exams.append(exam)
        
        tries = ExamTry.objects.filter(user=user, exam__in=course_exams).values('exam_id').annotate(max_hits=Max('hits')).order_by()
        
        for t in tries:
            exam = Exam.objects.get(pk=t['exam_id'])
            exams.append({
                'exam': exam,
                'hits': t['max_hits']
            })
        
        return exams
        
        
class Unit(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    course = models.ForeignKey(Course, related_name='units', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name
    
    def num_videos(self):
        return self.videos.count()
    
    class Meta:
        ordering = ['name']
    
    
class Enrollment(models.Model):
    IN_PROGRESS_STATUS = 0
    DONE_STATUS = 1
    
    STATUS_CHOICES = (
        (IN_PROGRESS_STATUS, 'Em andamento'),
        (DONE_STATUS, 'Concluído')
    )
        
    user = models.ForeignKey(get_user_model(), related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=IN_PROGRESS_STATUS, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def update_status(self):
        course_completed = True
        num_watched_videos_by_user = self.course.num_watched_videos_by_user(self.user)
        num_videos = self.course.num_videos()
        course_exams = list()
        
        for unit in self.course.units.all():
            exams = unit.exams.all()
            for exam in exams:
                course_exams.append(exam)
        
        for exam in course_exams:
            exam_try = ExamTry.objects.filter(user=self.user, exam=exam).values('exam_id').annotate(max_hits=Max('hits')).order_by()            
            exam_num_questions = exam.questions.count()
            if not exam_try or exam_try[0]['max_hits'] == 0 or ((exam_num_questions / exam_try[0]['max_hits']) < 0.70):
                course_completed = False 
        
        if num_watched_videos_by_user < num_videos:
            course_completed = False
            
        if course_completed:
            self.status = 1
            self.save()                

    
class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=upload_to_dir,
                            blank=True, null=True,
                            validators=[
                                FileValidator(
                                    max_size=100 * 1024 * 1024,
                                    allowed_extensions=('pdf'),
                                    allowed_mimetypes=('application/pdf')
                                )]
                            )
    unit = models.ForeignKey(Unit, related_name='documents', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    

    
class Video(models.Model):
    name = models.CharField(max_length=100)
    embedded = models.TextField('URL', blank=True)
    file = models.FileField(upload_to=upload_to_dir,
                            blank=True, null=True,
                            validators=[
                                FileValidator(
                                    max_size=100 * 1024 * 1024,
                                    allowed_extensions=('mp4', 'ogg', 'webm'),
                                    allowed_mimetypes=('video/mp4', 'video/ogg', 'video/webm')
                                )]
                            )
    unit = models.ForeignKey(Unit, related_name='videos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def is_embedded(self):
        return bool(self.embedded)
    
    def __str__(self):
        return self.name    

    
class WatchedVideos(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='watchedvideos', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='watched', on_delete=models.CASCADE)
    times = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Exam(models.Model):
    title = models.CharField(max_length=100, null=False)
    unit = models.ForeignKey(Unit, related_name='exams', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.title


class ExamTry(models.Model):    
    exam = models.ForeignKey(Exam, related_name='tries', on_delete=models.CASCADE, null=False) 
    user = models.ForeignKey(get_user_model(), related_name='tries', on_delete=models.CASCADE) 
    hits = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Question(models.Model):
    statement = models.TextField(max_length=500)
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.statement    
   
    
class Alternative(models.Model):
    description = models.TextField(max_length=500)
    question = models.ForeignKey(
        Question,
        related_name='alternatives',
        on_delete=models.CASCADE, null=False
    )
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description    

    
class Answer(models.Model):
    exam_try = models.ForeignKey(ExamTry, related_name='answers', on_delete=models.CASCADE, null=False)
    alternative = models.ForeignKey(Alternative, related_name='answers', on_delete=models.CASCADE, null=False)
    hit_the_answer = models.BooleanField(default=False) 
