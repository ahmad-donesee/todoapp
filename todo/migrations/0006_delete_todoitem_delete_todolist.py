# Generated by Django 5.0.3 on 2024-03-20 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_todoitem_todolist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ToDoItem',
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]