# Generated by Django 2.0.5 on 2018-06-05 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('courses', '0002_auto_20180525_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_taggedcourse_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
