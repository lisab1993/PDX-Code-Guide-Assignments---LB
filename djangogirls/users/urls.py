from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('registration/', views.registration_page, name='registration'),
    path('login/', views.login_page, name='login'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]


# there needs to be a path for the registration page, 
# as well as to perform the registration
# same for logging in
# don't forget an log out page
