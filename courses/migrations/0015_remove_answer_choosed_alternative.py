# Generated by Django 2.1 on 2018-08-21 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20180821_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choosed_alternative',
        ),
    ]
