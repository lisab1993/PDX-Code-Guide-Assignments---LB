from django.urls import path
from . import views

app_name = 'pokedex'
urlpatterns = [
    path('', views.index_vue, name="index_vue"),
    path('get_pokemon/', views.get_pokemon, name="get_pokemon")
]
