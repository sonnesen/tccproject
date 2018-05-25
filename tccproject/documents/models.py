from django.db import models
from courses.models import Course
from django.utils.text import slugify

def upload_to_dir(instance, filename):
    course_name = slugify(instance.course.name)
    return 'docs/courses/{0}/{1}'.format(course_name, filename)
    
class Document(models.Model):
    name = models.CharField(max_length=100)
    uri = models.FileField(upload_to=upload_to_dir)
    course = models.ForeignKey(Course, related_name='documents', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
