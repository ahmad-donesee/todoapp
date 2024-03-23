from django import forms

from .models import ToDoItem,ToDoList

class TodolistForm(forms.ModelForm):
    class Meta:
        model=ToDoList
        fields=['title','slug']

class TodoitemForm(forms.ModelForm):
    class Meta:
        model=ToDoItem
        fields=['title','content','time_todo','slug']
    