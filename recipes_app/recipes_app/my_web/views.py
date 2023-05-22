from django.shortcuts import render, redirect

from recipes_app.my_web.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipes_app.my_web.models import Recipe


def index(request):
    all_recipes = Recipe.objects.all()

    context = {
        'all_recipes': all_recipes,
    }

    return render(
        request,
        'index.html',
        context,
    )


def create(request):
    if request.method == 'GET':
        form = RecipeCreateForm()
    else:
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'create.html',
        context,
    )


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeEditForm(instance=recipe)
    else:
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(
        request,
        'edit.html',
        context,
    )


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeDeleteForm(instance=recipe)
    else:
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(
        request,
        'delete.html',
        context,
    )


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    print(recipe.ingredients)
    ingredients = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(
        request,
        'details.html',
        context,
    )
