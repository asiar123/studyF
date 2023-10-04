# Generated by Django 3.2 on 2023-10-02 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='matery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matematicas1', models.CharField(max_length=100, null=True)),
                ('Matematicas2', models.CharField(max_length=100, null=True)),
                ('Matematicas3', models.CharField(max_length=100, null=True)),
                ('Matematicas4', models.CharField(max_length=100, null=True)),
                ('Matematicas5', models.CharField(max_length=100, null=True)),
                ('Matematicas6', models.CharField(max_length=100, null=True)),
                ('Matematicas7', models.CharField(max_length=100, null=True)),
                ('Matematicas8', models.CharField(max_length=100, null=True)),
                ('Matematicas9', models.CharField(max_length=100, null=True)),
                ('Matematicas10', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
            },
        ),
    ]