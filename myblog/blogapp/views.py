from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import BlogPost

# Create your views here.
def index(request):
    #grabs all info pertaining to blog posts.
    posts = BlogPost.objects.all()
    for post in posts:
        print(post.title)
        print(post.body)
    # titles = BlogPost.objects.all()
    print(posts)

    context = {
        'message':'this is the blog!!!',
        'posts':posts,
        # 'titles':titles,
    }
    return render(request, "blogapp/index.html", context)

def created_date(request):
    blog_creation = timezone.now()
    return HttpResponse("This is the created date view")


