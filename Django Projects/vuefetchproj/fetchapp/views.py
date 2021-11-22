from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import BlogPost

def index(request):
    return render(request, 'fetchapp/index.html')


def get_posts(request):
    # get all blog posts from the database
    all_posts = BlogPost.objects.all()

    post_data = []
    for post in all_posts:
        post_data.append({
            'id': post.id,
            'title': post.title,
            'author': post.author,
            'body': post.body
        })

    return JsonResponse({'posts': post_data})