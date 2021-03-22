from django.core.management.base import BaseCommand
from pokedex.models import Pokemon
import requests
from io import BytesIO
from django.core import files
import json

#This command will load the pokemon.json file into the database.


class Command(BaseCommand):
    def handle(self, *args, **options):
        # delete everything at the start
        #this was also tested successfully
        Pokemon.objects.all().delete()

        # Open the file with the pokemon in json in reacing mode
        # The with statement guarantees the file will be closed after the with statement ends.
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            # Read the contents of the file
            contents = file.read()
            # print(contents ) ##this worked

            # Parse the json string
        data = json.loads(contents)
        # loop over the json string, and get the data from it
        for monster in data['pokemon']:
            number = monster['number']
            name = monster['name']
            height = monster['height']
            weight = monster['weight']
            image_front = monster['image_front']
            image_back = monster['image_back']
            types = monster['types']
            url = monster['url']
            monster = Pokemon(number=number, name=name, height=height,
                              weight=weight, image_front=image_front, image_back=image_back,
                              types=types, url=url)

            monster.save()
