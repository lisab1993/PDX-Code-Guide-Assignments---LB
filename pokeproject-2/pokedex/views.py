 
from django.shortcuts import render
from .models import Pokemon
from django.http import HttpResponse,  JsonResponse
import json
from django.core.paginator import Paginator
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

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
    monsters = Pokemon.objects.order_by('name')
    #total number of pages starts at 1
    num_pages = 1
    #get the number of monsters
    total_monsters = monsters.count()

    #pagination
    if 'page' in request.GET:
        #show the first page when the site loads
        page = request.GET.get('page')
        #show 20 pokemon on each page
        paginator = Paginator(monsters, 20) 
        
        monsters = paginator.page(page)
        num_pages = paginator.num_pages

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


    # return the data in json format
    return JsonResponse({'monsters': pokemon_list, 'num_pages': num_pages, })

