from django.db import models
from django.urls import reverse





class Item(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.id})
    
# Create your models here.
class Pokemon(models.Model):
   #Django uses the field types to apply automatic data validation in forms,
    #charfield is A string field, for small- to large-sized strings with enforced limits.
    #textfield is for storing large amounts of text (no required max_length)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("pokemon-detail", kwargs={"pokemon_id": self.id})
    
