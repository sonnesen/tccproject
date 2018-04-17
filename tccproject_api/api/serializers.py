from rest_framework import serializers

from api.models import Category, Unit, Activity, Resource, Test,\
    Question, Alternative
from api.models import Course, Instructor


class CourseSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Course
        fields = ('id', 'title', 'created_at', 'category', 'instructor', 'keywords')
        read_only_fields = ('created_at',)
        

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'name')
         
 
class InstructorSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Instructor
        fields = ('id', 'name', 'contact', 'about')
         
         
class UnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Unit
        fields = ('id', 'title', 'course')
        
        
class ResourceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resource
        fields = ('id', 'type', 'uri', 'activity')
        
                 
class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Activity
        fields = ('id', 'title', 'unit') 
           
           
class TestSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Test
        fields = ('id', 'unit')        
         
         
class QuestionSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Question
        fields = ('id', 'statement', 'test')
         
         
class AlternativeSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Alternative
        fields = ('id', 'description', 'answer', 'question', 'is_correct_answer')        

