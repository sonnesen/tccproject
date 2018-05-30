# Generated by Django 2.0.5 on 2018-05-24 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('units', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('uri', models.URLField(max_length=2000)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='units.Unit')),
            ],
        ),
    ]