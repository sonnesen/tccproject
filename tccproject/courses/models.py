from django.db import models
from taggit.managers import TaggableManager

from categories.models import Category
from instructors.models import Instructor


class Course(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, related_name='instructors', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='img/courses', null=True, blank=True)    
    keywords = TaggableManager('keywords')
        
    def __str__(self):
        return self.title