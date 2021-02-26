from django.urls import path
from . import views

app_name = "vuetodoapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("get_todoitems", views.get_todoitems, name="get_todoitems"),
    path("savetodo/", views.savetodo, name="savetodo")
]


