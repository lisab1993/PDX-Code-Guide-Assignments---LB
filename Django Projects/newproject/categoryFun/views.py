from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Fruit_Name, Fruit_Color

def index(request):
    latest_fruit_list = Fruit_Name.objects.order_by('-associated_date')[:5]
    output = ', '.join([q.title_text for q in latest_fruit_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    response = (f"You're looking at the results of {question_id}.")
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


