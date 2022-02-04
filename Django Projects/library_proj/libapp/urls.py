from django.urls import path
from . import views

app_name = 'libapp'
urlpatterns = [
    path('', views.index, name='index'),
]
