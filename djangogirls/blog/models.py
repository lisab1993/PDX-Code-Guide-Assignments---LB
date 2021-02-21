from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post (models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField( upload_to='images/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=350)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    