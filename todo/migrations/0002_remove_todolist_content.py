# Generated by Django 5.0.3 on 2024-03-19 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='content',
        ),
    ]