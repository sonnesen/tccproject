# Generated by Django 2.1 on 2018-08-21 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_examtry'),
    ]

    operations = [
        migrations.AddField(
            model_name='examtry',
            name='hits',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
