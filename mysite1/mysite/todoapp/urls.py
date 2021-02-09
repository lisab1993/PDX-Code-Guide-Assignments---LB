from django.urls import path
from . import views


app_name = "todoapp"
urlpatterns = [
    #name refers to the views.py
    path('', views.index, name='index'),
    path('saveitem/', views.save_todo_item, name='saveitem')
]