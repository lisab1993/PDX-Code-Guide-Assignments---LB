from django.shortcuts import render, reverse
from .models import ToDoItem
from django.http import HttpResponse, JsonResponse
import json


def index(request):
    return render(request, "vuetodoapp/index.html")


def get_todoitems(request):
    todoitems = ToDoItem.objects.all().order_by("-id")
    todo_data = []
    for todoitem in todoitems:
        todo_data.append({
            "title": todoitem.title,
            "task": todoitem.task,
        })
    return JsonResponse({ "todoitems":todo_data })

def savetodo(request):
    todo_data = json.loads(request.body)
    print(todo_data)
    title = todo_data["title"]
    task = todo_data["task"]
    todoitem = ToDoItem(title = title, task = task)
    todoitem.save()

    return HttpResponse("OK Morty")



# one view to render the template
# one to respond to json

    # title = models.CharField(max_length=200)
    # task = models.CharField(max_length=200)
