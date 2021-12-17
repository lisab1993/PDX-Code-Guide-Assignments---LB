from django.db import models


class Tuning(models.Model):
    name = models.CharField(max_length=100)
    root = models.CharField(max_length=10)

    def __str__(self):
        return self.name
