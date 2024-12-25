# Generated by Django 5.1.4 on 2024-12-25 16:30

import django.db.models.deletion
import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('overview', models.CharField(max_length=500, verbose_name='Описание')),
                ('text', models.CharField(blank=True, max_length=5000, verbose_name='Текстовое содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('D:/programming/web/django_projects/api_practice/edu/media'), verbose_name='Изображение')),
                ('order', models.PositiveBigIntegerField(verbose_name='Номер модуля')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Модуль',
                'verbose_name_plural': 'Модули',
                'ordering': ['-updated_at'],
            },
        ),
    ]