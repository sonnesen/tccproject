# Generated by Django 2.1 on 2018-08-21 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_examtry_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='status',
        ),
    ]
