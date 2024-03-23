# Generated by Django 5.0.3 on 2024-03-20 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todolist_time_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='todolist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todolist', to='todo.todolist'),
        ),
    ]