from django.template.library import Library

from courses.models import Enrollment, Course, Unit
from django.template.defaultfilters import stringfilter

register = Library()


def get_user_courses(user):
    enrollments = Enrollment.objects.filter(user=user).all()
    courses = []    
    for enrollment in enrollments:
        course = Course.objects.get(pk=enrollment.course.pk)
        courses.append(course)    
    return courses


@register.inclusion_tag('templatetags/user_menu_courses.html')
def user_menu_courses(user):
    courses = get_user_courses(user)        
    context = { 'courses': courses }
    return context


@register.inclusion_tag('templatetags/user_courses.html')
def user_courses(user):
    courses = get_user_courses(user)        
    context = { 'courses': courses }    
    return context


def get_course_units(course):
    units = Unit.objects.filter(course=course).all()    
    return units


@register.inclusion_tag('templatetags/course_menu_units.html')
def course_menu_units(course):
    units = get_course_units(course)
    context = { 'units': units }    
    return context


@register.inclusion_tag('templatetags/course_units.html')
def course_units(course):
    units = get_course_units(course)        
    context = { 'units': units }    
    return context


@register.simple_tag
def convert_ascii_to_string(code):
    return chr(code)


@register.filter(is_safe=True)
@stringfilter
def concat_str(value, arg):
    return "{}{}".format(value, arg)
