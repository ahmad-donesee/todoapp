# Generated by Django 5.0.3 on 2024-03-19 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todolist_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='time_todo',
        ),
    ]
