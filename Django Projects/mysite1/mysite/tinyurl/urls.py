from django.urls import path, include
from . import views


app_name = 'tinyurl'
urlpatterns = [
    path('', views.index, name='index'),
    path('saving', views.save_shortened, name='saving'),
    path('redirection/<str:code>', views.redirection, name = 'redirection'),
    path('delete/<int:url_item_id>/', views.delete_item, name='delete_item'),
]