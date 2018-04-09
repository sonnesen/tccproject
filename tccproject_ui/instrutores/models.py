from django.db import models


class Instrutor(models.Model):
    nome = models.CharField(max_length=100, null=False)

