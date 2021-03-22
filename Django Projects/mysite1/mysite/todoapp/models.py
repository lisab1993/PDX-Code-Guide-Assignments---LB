from django.db import models


# Create your models here.

class Priority(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
