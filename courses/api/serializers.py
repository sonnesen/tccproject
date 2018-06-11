from rest_framework.serializers import ModelSerializer

from categories.models import Category
from courses.models import Course
from instructors.models import Instructor
from categories.api.serializers import CategorySerializer
from instructors.api.serializers import InstructorSerializer
from taggit_serializer.serializers import TagListSerializerField,\
    TaggitSerializer


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
            category, created = Category.objects.get_or_create(**category_data)

        if instructor_data:
            instructor, created = Instructor.objects.get_or_create(**instructor_data)

        course = Course.objects.create(**validated_data)
        course.category = category
        course.instructor = instructor
        course.save()

        return course

