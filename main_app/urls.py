from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemon_index, name='pokemon-index'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='pokemon-detail'),
    path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon-create'),
    path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon-update'),
    path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon-delete'),
    path('items/create/', views.ItemCreate.as_view(), name='item-create'),
    path('item/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('item/', views.ItemList.as_view(), name='item-index'),
    path('pokemon/<int:pokemon_id>/remove-item/<int:item_id>/', views.remove_item, name='remove-item'),

    path('pokemon/<int:pokemon_id>/associate-item/<int:item_id>/', views.associate_item, name='associate-item'),
    path('accounts/signup/', views.signup, name='signup'),


]