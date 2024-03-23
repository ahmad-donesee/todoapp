from django.contrib import admin
from .models import ToDoItem,ToDoList


@admin.register(ToDoList)
class AdminToDoList(admin.ModelAdmin):
    list_display=( 'title',)
    search_fields = ['title']
    prepopulated_fields={'slug':("title",),}
    
@admin.register(ToDoItem)
class AdminToDoItem(admin.ModelAdmin):
    list_display=( 'title','time_todo')
    search_fields = ['title']
    prepopulated_fields={'slug':("title",),}
