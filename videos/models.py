from django.db import models

from units.models import Unit


class Video(models.Model):
    name = models.CharField(max_length=100)
    uri = models.URLField(max_length=2000)
    unit = models.ForeignKey(Unit, related_name='videos', 
                             on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
