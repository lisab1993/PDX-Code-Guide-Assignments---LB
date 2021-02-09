from django.db import models
import datetime

# Create your models here.

class Priority(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    created_date = models.DateField(null=True)

    def __str__(self):
        return self.text
