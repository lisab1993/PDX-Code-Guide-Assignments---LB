from django.urls import path
from . import views


app_name = 'tinyurl'
urlpatterns = [
    path('', views.index, name='index'),
    path('saving', views.save_shortened, name='saving'),
]