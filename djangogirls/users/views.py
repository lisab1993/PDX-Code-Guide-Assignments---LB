from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def registration_page(request):
    # return HttpResponse('hello')
    return render(request, 'users/register.html', {})


def login_page(request):
    return render(request, 'users/login.html', {})


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

    # check if the username already exists
    if User.objects.filter(username=username).exists():
        return render(request, 'users/register.html', {'display': 'Username not available'})

    if len(password)<6:
        return render(request, 'users/register.html', {'display': 'Passwords must be at least 6 characters long'})

    # create a variable with the components needed to log in.
    user = User.objects.create_user(username=username, password=password, email=email)
    return HttpResponseRedirect(reverse('blog:post_list'))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('blog:post_list'))
    else:
        return render(request, 'users/login.html', {'display': 'The username or password is incorrect, please try again'})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
