# main_app/views.py

from django.shortcuts import render
from .models import Pokemon, Item
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Define the home view function 
#reqeust is similar to the req object in express
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/index.html',{'pokemons': pokemons})

def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    items_pokemon_doesnt_have = Item.objects.exclude(id__in = pokemon.items.all().values_list('id'))
    return render(request, 'pokemon/detail.html',{
        'pokemon': pokemon,
        'Items': items_pokemon_doesnt_have
    })
def associate_item(request, pokemon_id, item_id):
    # Note that you can pass a toy's id instead of the whole object
    Pokemon.objects.get(id=pokemon_id).toys.add(item_id)
    return redirect('pokemon-detail', pokemon_id=pokemon_id)


class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['name', 'type', 'description']
class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'   
class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
class ItemList(ListView):
    model = Item
class ItemDetail(DetailView):
    model = Item