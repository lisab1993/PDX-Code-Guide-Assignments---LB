from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .forms import PostForm
#@login_required will require the user to be logged in for a view to work
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# @login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def profile(request):
    #  return HttpResponse('hello')
    logged_user = request.user
    user_posts = Post.objects.filter(author = logged_user)
    
    context = {
        'user_posts':user_posts
    }
    return render(request, 'blog/profile.html', context)





#register 
#  no special parameters
# path('registration', views.register_user, name='registration'),

#login 
# password as a parameter from the user database required for access
# path('login/<str:password>', views.login_user, name='login'),


# profile 
# only allow the user to see their own profile
#view profiles by the id
# path('profile/<int:user_id>', views.profile_user, name='profile')