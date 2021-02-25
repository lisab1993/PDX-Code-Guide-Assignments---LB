from django.db import models

# Create your models here.


class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=500)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=700)
    image_back = models.CharField(max_length=700)
    types = models.CharField(max_length=700)
    url = models.CharField(max_length=700, default ='https://pokemon.fandom.com/wiki/Pok%C3%A9mon_Wiki')

    def __str__(self):
        return self.name
    