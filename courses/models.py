from django.contrib.auth import get_user_model
from django.db import models
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


class Unit(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    course = models.ForeignKey(Course, related_name='units', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name
    
    
class Enrollment(models.Model):
    
    user = models.ForeignKey(get_user_model(), related_name='+', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
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
    user = models.ForeignKey(get_user_model(), related_name='+', on_delete=models.CASCADE)
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
    user = models.ForeignKey(get_user_model(), related_name='+', on_delete=models.CASCADE) 
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
