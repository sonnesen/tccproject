from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    category = models.ForeignKey('Category', related_name='categories', on_delete=models.CASCADE)
    instructor = models.ForeignKey('Instructor', related_name='instructors', on_delete=models.SET_NULL, null=True)
    keywords = models.CharField(max_length=100, null=True)
        
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)
        db_table = 'course'
        
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
        db_table = 'category'        
    
    
class Instructor(models.Model):
    name = models.CharField(max_length=100, null=False)
    contact = models.CharField(max_length=100, null=False)
    about = models.TextField(max_length=200, null=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
        db_table = 'instructor'
        
    
class Unit(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey('Course', related_name='units', on_delete=models.CASCADE, null=False)
        
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'unit'
        ordering = ['id']
    
    
class Activity(models.Model):
    title = models.CharField(max_length=100)
    unit = models.ForeignKey('Unit', related_name='activities', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'activity'
        ordering = ['id']
    

class Resource(models.Model):
    uri = models.URLField(max_length=2000)
    activity = models.OneToOneField('Activity', related_name='resource', on_delete=models.CASCADE, null=True)
    
    VIDEO_TYPE = 1
    DOCUMENT_TYPE = 2
    
    TYPES = (
        (VIDEO_TYPE, 'Video'),
        (DOCUMENT_TYPE, 'Document')
    )
    
    type = models.SmallIntegerField(choices=TYPES)
    
    class Meta:
        db_table = 'resource'
        ordering = ['id']
       
        
class Test(models.Model):
    title = models.CharField(max_length=100, null=False)
    unit = models.ForeignKey('Unit', related_name='tests', on_delete=models.SET_NULL, null=True)
     
    class Meta:
        db_table = 'test'
        ordering = ['id']
        
    def __str__(self):
        return self.title

class Question(models.Model):
    statement = models.TextField(max_length=500)
    test = models.ForeignKey('Test', related_name='questions', on_delete=models.CASCADE, null=False)
    
    class Meta:
        db_table = 'question'
        ordering = ['id']
        
    def __str__(self):
        return self.statement
        

class Alternative(models.Model):
    description = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    question = models.ForeignKey('Question', related_name='alternatives', on_delete=models.CASCADE, null=False)
    is_correct_answer = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'alternative'
        ordering =['id']
        