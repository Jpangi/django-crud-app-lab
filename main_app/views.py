# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function 
#reqeust is similar to the req object in express
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

class Pokemon:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

pokemons = [
    Pokemon('Pikachu', 'Electric', 'small mouse'),
    Pokemon('Bulbasor', 'Grass', 'leafy'),
    Pokemon('Charmander', 'Fire', 'fire lizard'),
    Pokemon('Squirtle', 'Water', 'turtle'),
]

def pokemon_index(request):
    return render(request, 'pokemon/index.html',{'pokemons': pokemons})