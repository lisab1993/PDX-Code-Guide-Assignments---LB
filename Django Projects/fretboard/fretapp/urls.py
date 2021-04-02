from django.urls import path
from . import views

fretapp = 'fretapp'
urlpatterns = [
    path('', views.index, name='index'),
]
