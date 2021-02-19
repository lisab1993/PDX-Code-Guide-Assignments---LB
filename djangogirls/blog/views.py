from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, BlogPost
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})



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
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})



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
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})





    # author = models.ForeignKey(User, on_delete=models.PROTECT)
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)



@login_required
def profile(request):
    #  return HttpResponse('hello')
    logged_user = request.user
    user_posts = Post.objects.filter(author = logged_user)
    
    context = {
        'user_posts':user_posts
    }
    return render(request, 'blog/profile.html', context)



