from django.db import models
from django.urls import reverse



class ToDoList(models.Model):
    title=models.CharField(max_length=100)
    update=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True)
    
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    

class ToDoItem(models.Model):
    todolist=models.ForeignKey(ToDoList,related_name="todolist",on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    update=models.DateTimeField(auto_now=True)
    time_todo=models.DateTimeField()
    slug=models.SlugField(unique=True)
    
    def __str__(self):
        return f"{self.title}"