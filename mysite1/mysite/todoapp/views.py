from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Priority, TodoItem
from django.utils import timezone

def index(request):
    #gets everything from the TodoItem Model, and puts them in order based on their creation date
    todo_items = TodoItem.objects.filter(completed=False).order_by('created_date')
    #all priority id's 
    completed_items = TodoItem.objects.filter(completed=True).order_by('completed_date')
    priorities = Priority.objects.all()
    print(priorities)
    #all the computer-generated id's for priorities are in this variable.
    context = {
        "todo_items": todo_items,
        "priorities": priorities,
        "completed_items": completed_items
    }

    return render(request, "todoapp/index.html", context)

def save_todo_item(request):
    # print(request.POST)
    text = request.POST['text']
    created_date = timezone.now()
    # created_date = request.POST['created_date']

    #has to do with the form. 
    priority_id = request.POST.get('priority')
    priority = Priority.objects.get(id=priority_id)
    # print(priority)
    # print(priority_id)
    # priority = Priority.objects.get(id=priority_id)

    #creating an instance of the model using data
    show_item = TodoItem(text = text, created_date = created_date, completed_date=None, priority = priority)
    #save the model to the database
    show_item.save()
    #remain on the index page
    return HttpResponseRedirect(reverse("todoapp:index"))

#anytime you submit a form, do a redirect. It's good practice and causes fewer errors

def delete_item(request, todoitem_id):
    # look up the todo item with the given id
    todo_item = TodoItem.objects.get(id=todoitem_id)

    #set the completion date
    completed_date = timezone.now()

    # delete it
    todo_item.delete()


    # redirect back to the index page
    return HttpResponseRedirect(reverse("todoapp:index"))
    # return HttpResponse('you are deleting the todo item with id ' + str(todoitem_id))


def complete_item(request, todoitem_id):
    #grab the item with the given id
    todo_item = TodoItem.objects.get(id=todoitem_id)

    #mark it as complete (and remove it from the todo list)
    todo_item.completed = True

    #set the completion date
    todo_item.completed_date = timezone.now()
    
    # save it to the new list 
    todo_item.save()

    #redirect to the index page
    return HttpResponseRedirect(reverse("todoapp:index"))
