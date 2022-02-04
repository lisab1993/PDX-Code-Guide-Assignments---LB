from django.urls import path

from . import views

app_name = 'kittens_app'
urlpatterns = [
    path('', views.index, name="index")
]
