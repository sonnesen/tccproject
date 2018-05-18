from django.db import models
from exams.models import Exam

class Question(models.Model):
    statement = models.TextField(max_length=500)
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.statement
