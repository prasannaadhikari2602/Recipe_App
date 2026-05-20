from django.shortcuts import render
from .models import Recipe
# Create your views here.

def home(request):
    
    recipes = Recipe.objects.all()
    
    context = {
        "Recipes" : recipes
    }
    return render(request, 'home/home.html', context)