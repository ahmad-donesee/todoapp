# Generated by Django 5.0.3 on 2024-03-20 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todoitem_todolist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='todolist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todolist', to='todo.todolist'),
        ),
    ]
