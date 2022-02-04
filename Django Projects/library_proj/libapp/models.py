from turtle import title
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

    @property
    def available(self):
        return self.trackings.last()

    
class Tracking(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='trackings')
    user = models.CharField(max_length=150)
    checkout = models.BooleanField()
    timestamp = models.DateTimeField()

    def __str__(self):
        if self.checkout == True:
            status = 'checked out (unavailable)'
        else:
            status = 'checked in (available)'
        return self.book.title + " - " + status
    