from django.urls import path
from . import views


app_name = 'categoryFun'
urlpatterns = [
    path('index/', views.index, name='index'),
]