from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, BlogPost
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@login_required
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def show_create(request):
    return render(request, 'blog/post_create.html')


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.image = request.FILES.get('image', None)
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # prevent users from editing other's posts 
    if post.author != request.user:
        raise Http404
    #what to do when the form is either successful or unsuccessful
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #the user selected an image when they were editing the post
            #now we are checking to see if that image exists, or it's it null.
            if 'image' in request.FILES:
                post.image = request.FILES.get('image')
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    #how to clear the image
    if 'clear_image' in request.POST:
        post.image = None
    elif 'image' in request.FILES:
        image = request.FILES['image']
        post.image = image
    
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def profile(request):
    #  return HttpResponse('hello')
    user = authenticate(username=request.user, password=request.user)
    logged_user = request.user
    user_posts = Post.objects.filter(author=logged_user)

    context = {
        'user_posts': user_posts
    }
    return render(request, 'blog/profile.html', context)


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #only let users delete their own posts
    if post.author != request.user:
        raise Http404
    #if they are the author, delete the post and go back to the profile view.
    post.delete()
    return redirect('blog:profile')

