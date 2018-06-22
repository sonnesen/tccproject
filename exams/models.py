from django.db import models

from units.models import Unit


class Exam(models.Model):
    title = models.CharField(max_length=100, null=False)
    unit = models.ForeignKey(Unit, related_name='exams', 
                             on_delete=models.SET_NULL, null=True)
     
    def __str__(self):
        return self.title
