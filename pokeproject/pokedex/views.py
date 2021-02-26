from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Pokemon
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
import json
import string


# For each pokemon, generate a table showing all of the information
# Use <img src="..."> to display their front and back image.
# only show 20 pokemon at a time using pagination


def index_vue(request):
    ''' Renders the index page for vue, but does not grab the data itself '''
    # return HttpResponse('ok') #Successful
    return render(request, 'pokedex/index_vue.html', {})

def get_pokemon(request):
    ''' Returns the pokemon data in json format '''
    # return HttpResponse('ok') #Successful

    # grab all of the pokemon
    monsters = Pokemon.objects.order_by('number')

    # create a list that grabs all of their fields from the model
    pokemon_list = []
    for monster in monsters:
        pokemon_list.append({
            'number': monster.number,
            'name': monster.name.title(),
            'height': monster.height,
            'weight': monster.weight,
            'image_front': monster.image_front,
            'image_back': monster.image_back,
            'types': monster.types,
            'url': monster.url,
        })
    # return the data as json
    return JsonResponse({'monsters': pokemon_list})
