from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
# @login_required will require the user to be logged in for a view to work
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# The last parameter, {}, is a place in which we can add some things for
# the template to use. We need to give them names
# (we will stick to 'posts' right now).: )
# It should look like this: {'posts': posts}.
# Please note that the part before : is a string; you need to wrap it with quotes: ''.

# Create your views here.


def registration_page(request):
    # return HttpResponse('hello')
    return render(request, 'users/register.html', {})


def login_page(request):
    return render(request, 'users/login.html', {})


def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    # check if the username already exists
    if User.objects.filter(username=username).exists():
        return render(request, 'users/register.html', {'display': 'Username not available'})

    # create a variable with the components needed to log in.
    user = User.objects.create_user(username, password=password, email=email)
    return HttpResponseRedirect(reverse('blog:post_list'))

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('blog:post_list'))
    else:
        return render(request, 'users/login.html', {'display':'The username or password is incorrect, please try again'})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

