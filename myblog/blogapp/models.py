from django.db import models
from django.utils import timezone

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)

    