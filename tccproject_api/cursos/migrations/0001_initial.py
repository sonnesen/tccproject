# Generated by Django 2.0.4 on 2018-04-09 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('criado_em', models.DateField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='cursos.Categoria')),
            ],
            options={
                'ordering': ('criado_em',),
            },
        ),
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=100)),
                ('resumo', models.TextField(max_length=200)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='instrutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='cursos.Instrutor'),
        ),
    ]
