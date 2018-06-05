# Generated by Django 2.0.5 on 2018-06-05 02:13

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_taggedcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='keywords',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='courses.TaggedCourse', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
