from django.shortcuts import render,redirect
from .models import Recipes
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.
def home(request):
    return render(request,'app/option.html')


def register(request):
    return render(request,'app/registration.html')


def login_data(request):
    if request.method == "POST" :
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'],
                                        email=request.POST['email'],
                                        first_name = request.POST['first_name'],
                                        last_name = request.POST['last_name'])
        user.set_password('password')
        #user.save()
    return render(request,'app/login.html')


def check(request):
    #import pdb; pdb.set_trace()
    user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
    print(user)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/app/recipe_list/')
    else:
        return HttpResponseRedirect('/app/register/')


def logout_data(request):
    logout(request)
    return HttpResponseRedirect('/app/login/')


@login_required(login_url='/app/login/')
def recipe_list(request):
    recipe = Recipes.objects.all()
    return render(request,'app/recipe_details.html', {"recipes": recipe})


@login_required(login_url='/app/login/')
def create(request):
    return render(request,'app/create.html')


@login_required(login_url='/app/login/')
def data(request):
    Recipes.objects.create(name = request.POST["name"],
                           ingredients = request.POST["ingredients"],
                           process = request.POST["process"],
                           image = request.FILES["image"])
    return HttpResponseRedirect('/app/recipe_list/')


@login_required(login_url='/app/login/')
def details(request,recipe_id):
    recipe = Recipes.objects.get(id = recipe_id)
    return render(request,'app/details.html',{'recipes':recipe})


@login_required(login_url='/app/login/')
def delete(request,recipe_id):
    Recipes.objects.get(id = recipe_id).delete()
    return HttpResponseRedirect('/app/recipe_list/',{recipe_id})


@login_required(login_url='/app/login/')
def my_view(request):
    if not request.user.is_authenticated:
        return render(request, 'app/error.html')
    else:
        return HttpResponseRedirect('/app/recipe_list/')