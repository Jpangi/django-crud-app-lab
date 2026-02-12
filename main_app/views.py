# main_app/views.py

from django.shortcuts import render
from .models import Pokemon, Item
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
# Define the home view function 
#reqeust is similar to the req object in express
# def home(request):
#     # Send a simple HTML response
#     return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

@login_required
def pokemon_index(request):
    pokemons = Pokemon.objects.filter(user=request.user)
    return render(request, 'pokemon/index.html',{'pokemons': pokemons})

@login_required
def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    items_pokemon_doesnt_have = Item.objects.exclude(id__in = pokemon.items.all().values_list('id'))
    return render(request, 'pokemon/detail.html',{
        'pokemon': pokemon,
        'items': items_pokemon_doesnt_have
    })

@login_required
def associate_item(request, pokemon_id, item_id):
    # Note that you can pass a toy's id instead of the whole object
    Pokemon.objects.get(id=pokemon_id).items.add(item_id)
    return redirect('pokemon-detail', pokemon_id=pokemon_id)
def remove_item(request, pokemon_id, item_id):
    Pokemon.objects.get(id=pokemon_id).items.remove(item_id)
    return redirect('pokemon-detail', pokemon_id=pokemon_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('pokemon-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class PokemonCreate(LoginRequiredMixin, CreateView):
    model = Pokemon
    fields = ['name', 'type', 'description']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the pokemon
        return super().form_valid(form)
    
class PokemonUpdate(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ['name', 'type', 'description']
class PokemonDelete(LoginRequiredMixin, DeleteView):
    model = Pokemon
    success_url = '/pokemon/'   
class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = '__all__'
class ItemList(LoginRequiredMixin, ListView):
    model = Item
class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item

class Home(LoginView):
    template_name = 'home.html'