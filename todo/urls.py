from django.urls import path
from .views import todolist,todoitem,delete_todo_list,todolist_update , delete_todo_item  #,todoitem_update

app_name="todo"

urlpatterns = [
    path("",todolist,name="todolist"),
    path("<int:id>/",todoitem,name="todoitem"),
    path("delete/<int:id>/",delete_todo_list,name="delete_todo_list"),
    path("delete/<slug:slug>/",delete_todo_item,name="delete_todo_item"),
    path("update/<int:id>/",todolist_update,name="todolist_update"),
    #path("edit/<int:todolist__id>/",todoitem_update,name="todoitem_update"),
    
]