from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/profile/', views.profile, name='profile'),
    path('post/create/', views.show_create, name="create"),
    # localhost:8000/post/5/delete/
    path('post/<int:pk>/delete/', views.delete, name="delete"),
] 

#register 
#  no special parameters
# path('registration', views.register_user, name='registration'),

#login 
# password as a parameter from the user database required for access


# profile 
# only allow the user to see their own profile
#view profiles by the id
# path('profile/<int:user_id>', views.profile_user, name='profile'),





# class BlogPost(models.Model):
#     title = models.CharField(max_length=350)
#     body = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     public = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_edited = models.DateTimeField(auto_now=True)

#User Database Components:
# id
# password
# last_login
# is_superuser
# username
# last_name
# email
# is_staff
# is_active
# date_joined
# first_name
