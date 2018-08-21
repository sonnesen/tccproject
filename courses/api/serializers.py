from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from taggit_serializer.serializers import TagListSerializerField, \
    TaggitSerializer

from courses.models import Course, Document, Category, Instructor, Unit, Video, \
    Exam, Question, Alternative


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')


class InstructorSerializer(ModelSerializer):

    class Meta:
        model = Instructor
        fields = ('__all__')

                
class DocumentSerializer(ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    
    class Meta:
        model = Document
        fields = ('__all__')

        
class CourseSerializer(TaggitSerializer, ModelSerializer):
    category = CategorySerializer()
    instructor = InstructorSerializer()
    keywords = TagListSerializerField()

    class Meta:
        model = Course
        fields = ('__all__')
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        category_data = validated_data.pop('category', None)
        instructor_data = validated_data.pop('instructor', None)

        if category_data:
            (category, created) = Category.objects.get_or_create(**category_data)

        if instructor_data:
            (instructor, created) = Instructor.objects.get_or_create(**instructor_data)

        course = Course.objects.create(**validated_data)
        course.category = category
        course.instructor = instructor
        course.save()

        return course

    
class VideoSerializer(ModelSerializer):
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
    
    class Meta:
        model = Video
        fields = ('__all__')    

        
class ExamSerializer(ModelSerializer):
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
    
    class Meta:
        model = Exam
        fields = ('__all__')      

        
class UnitSerializer(ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    
    class Meta:
        model = Unit
        fields = ('__all__')

        
class QuestionSerializer(ModelSerializer):
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())
    
    class Meta:
        model = Question
        fields = ('__all__')     

        
class AlternativeSerializer(ModelSerializer):
    """
    Classe responsável por serializar um objeto do tipo Alternative
    """
    
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all()
    )

    class Meta:
        model = Alternative
        fields = ('__all__')    

