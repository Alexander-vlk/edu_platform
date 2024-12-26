# Generated by Django 5.1.4 on 2024-12-26 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('courses', '0009_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ['text', 'video', 'image', 'file']}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Тип контента'),
        ),
    ]
