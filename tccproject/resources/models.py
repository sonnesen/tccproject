from django.db import models

from activities.models import Activity


class Resource(models.Model):
    uri = models.URLField(max_length=2000)
    activity = models.OneToOneField(Activity, related_name='resource', on_delete=models.CASCADE, null=True)
    
    VIDEO_TYPE = 1
    DOCUMENT_TYPE = 2
    
    TYPES = (
        (VIDEO_TYPE, 'Video'),
        (DOCUMENT_TYPE, 'Document')
    )
    
    type = models.SmallIntegerField(choices=TYPES)
