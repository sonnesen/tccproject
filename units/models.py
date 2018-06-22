from django.db import models

from courses.models import Course


class Unit(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    course = models.ForeignKey(Course, related_name='units', 
                               on_delete=models.CASCADE, null=False)
        
    def __str__(self):
        return self.name
