from django.shortcuts import render,redirect
from .models import ToDoList,ToDoItem
from .forms import TodolistForm,TodoitemForm
from django.http import HttpResponse

# show all to do list

def todolist(request):
    todolist=ToDoList.objects.all()
    form=TodolistForm()
    if request.method=="POST":
        form=TodolistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:todolist')
    else:
        return render(request,"todo/todolist.html",{"mylist":todolist,"form":form})

# show  one specific todo list and its items

def todoitem(request,id=None):
    list=ToDoList.objects.get(id=id)
    item=ToDoItem.objects.all().filter(todolist_id=list)
    # number=len(item)
    form=TodoitemForm()
    if request.method=="POST":
        form=TodoitemForm(request.POST)
        if form.is_valid():
            todolist=form.todolist_id=list
            form2=ToDoItem(todolist=todolist,time_todo=form.cleaned_data['time_todo'],title=form.cleaned_data['title'],content=form.cleaned_data['content'],slug=form.cleaned_data['slug'])
            form2.save()
            return redirect('todo:todoitem',id=list.id)
        return HttpResponse("your item of form is invalid")
    return render(request,"todo/todolist_item.html",{"item":item,"form":form})


# update the todo list
def todolist_update(request,id=None):
    todolist=ToDoList.objects.get(id=id)
    form=TodolistForm()
    if request.method=="POST":
        form=TodolistForm(request.POST)
        if form.is_valid():
            todolist.delete()
            title=form.cleaned_data['title']
            slug=form.cleaned_data['slug']
            todolist.title=title
            todolist.slug=slug
            todolist.save()
            return redirect('todo:todolist')
    else:
        return render(request,"todo/todolist_update.html",{"mylist":todolist,"form":form})




# def todoitem_update(request,todolist__id):
#     list1=ToDoItem.objects.get(id=todolist__id)
#     form=TodoitemForm()
#     if request.method=="POST":
#         form=TodoitemForm(request.POST)
#         if form.is_valid():
#             todolist=list1.todolist
#             list1.delete()
#             title=form.cleaned_data['title']
#             content=form.cleaned_data['content']
#             time_todo=form.cleaned_data['time_todo']
#             slug=form.cleaned_data['slug']
            
#             newlist=ToDoItem(todolist=todolist,title=title,content=content,time_todo=time_todo,slug=slug)
#             newlist.save()
#             return redirect('todo:todoitem',id=newlist.id)
#     return render(request,"todo/todolist_item_update.html",{"item":list1,"form":form})
    



def delete_todo_list(request,id):
    list=ToDoList.objects.get(id=id)
    list.delete()
    return redirect("todo:todolist")

def delete_todo_item(request,slug):
    list=ToDoItem.objects.get(slug=slug)
    list.delete()
    return redirect("todo:todoitem",id=list.todolist.id)



# 