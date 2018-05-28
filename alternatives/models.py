from django.db import models

from questions.models import Question


class Alternative(models.Model):
    description = models.TextField(max_length=500)
    question = models.ForeignKey(Question, related_name='alternatives', on_delete=models.CASCADE, null=False)
    is_correct = models.BooleanField(default=False)
    
    
