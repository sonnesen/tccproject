# Generated by Django 2.0.5 on 2018-05-23 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180522_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/courses'),
        ),
    ]