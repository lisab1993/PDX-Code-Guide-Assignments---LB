from django.urls import path
from . import views

fretapp = 'fretapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('index_vue/', views.index_vue, name='index_vue')
]
