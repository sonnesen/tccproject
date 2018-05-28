from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=100, null=False)
    contact = models.EmailField(max_length=100, null=False)
    about = models.TextField(max_length=200, null=False)

    def __str__(self):
        return self.name
