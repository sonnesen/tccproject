from django.db import models

from units.models import Unit


class Activity(models.Model):
    title = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit, related_name='activities', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
