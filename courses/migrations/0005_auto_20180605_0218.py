# Generated by Django 2.0.5 on 2018-06-05 02:18

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20180605_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggedcourse',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='taggedcourse',
            name='tag',
        ),
        migrations.AlterField(
            model_name='course',
            name='keywords',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='keywords'),
        ),
        migrations.DeleteModel(
            name='TaggedCourse',
        ),
    ]