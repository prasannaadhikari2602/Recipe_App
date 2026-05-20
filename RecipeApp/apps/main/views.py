from django.shortcuts import render,redirect
from .models import Recipe
# Create your views here.

def home(request):
    
    recipes = Recipe.objects.all()
    
    context = {
        "Recipes" : recipes
    }
    return render(request, 'home/home.html', context)

def add(request):

    if request.method == "POST":

        title = request.POST.get('title')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instruction = request.POST.get('instruction')
        total_time = request.POST.get('total_time')

        image = request.FILES.get('image')

        Recipe.objects.create(
            title=title,
            description=description,
            ingredients=ingredients,
            instruction=instruction,
            total_time=total_time,
            image=image
        )

        return redirect('recipe_list')

    return render(request, 'home/add.html')


def edit(request, ID):
      recipe = Recipe.objects.get(id = ID)
      if request.method == "POST":
        recipe.title = request.POST['title']
        recipe.description = request.POST['description']
        recipe.ingredients = request.POST['ingredients']
        recipe.instruction = request.POST['instruction']
        recipe.total_time = request.POST['total_time']

        # image optional update
        if 'image' in request.FILES:
            recipe.image = request.FILES['image']

        recipe.save()
        return redirect('recipe_list')

      return render(request, 'home/edit.html', {'recipe': recipe})
  
  
def delete(request, ID):

    recipe = Recipe.objects.get(id = ID)
    recipe.delete()
    return redirect('recipe_list')

    