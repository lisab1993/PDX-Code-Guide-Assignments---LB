from django.urls import path
from . import views


app_name = "todoapp"
urlpatterns = [
    #name refers to the views.py
    path('', views.index, name='index'),
    path('saveitem/', views.save_todo_item, name='saveitem'),
    # localhost:800/delete/5/, localhost:8000/delete/67/
    path('delete/<int:todoitem_id>/', views.delete_item, name='delete'),
    path('complete/<int:todoitem_id>/', views.complete_item, name='complete')
]