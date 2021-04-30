from django.shortcuts import render
from .models import Recipes
from django.http import HttpResponseRedirect

# Create your views here.
def recipe_list(request):
    recipe = Recipes.objects.all()
    return render(request,'app/recipe_details.html', {"recipes": recipe})
def create(request):
    return render(request,'app/create.html')
def data(request):

    Recipes.objects.create(name = request.POST["name"],
                           ingredients = request.POST["ingredients"],
                           process = request.POST["process"],
                           image = request.FILES["image"])
    return HttpResponseRedirect('/app/recipe_list/')
def details(request,recipe_id):
    recipe = Recipes.objects.get(id = recipe_id)
    return render(request,'app/details.html',{'recipes':recipe})
def delete(request,recipe_id):
    Recipes.objects.get(id = recipe_id).delete()
    return HttpResponseRedirect('/app/recipe_list/',{recipe_id})