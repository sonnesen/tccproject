# Generated by Django 2.0.4 on 2018-04-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180415_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='titulo',
            field=models.CharField(default='Avalição objetiva de Fixação', max_length=100, verbose_name='Título'),
            preserve_default=False,
        ),
    ]
