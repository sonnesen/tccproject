# Generated by Django 2.1 on 2018-08-29 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20180828_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['name']},
        ),
    ]
