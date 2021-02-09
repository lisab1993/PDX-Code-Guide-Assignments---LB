from django.shortcuts import render
from django.http import HttpResponse
from .models import Priority, TodoItem


def index(request):
    #gets everything from the TodoItem Model, and puts them in order based on their creation date
    todo_items = TodoItem.objects.order_by('created_date')
    #all priority id's 
    
    priorities = Priority.objects.all()
    #all the computer-generated id's for priorities are in this variable.
    context = {
        "todo_items": todo_items,
        "priorities": priorities,
    }
    return render(request, "todoapp/index.html", context)

def save_todo_item(request):
    print(request.Post)
    item = request.POST['text']
    created_date = request.POST['created_date']
    priority = request.POST['priority']
    #creating an instance of the model using data
    show_item = TodoItem(item = item, created_date = created_date, priority = priority)
    #save the model to the database
    show_item.save()
    #remain on the index page
    return render(request, 'todoapp/save_todo_item.html')