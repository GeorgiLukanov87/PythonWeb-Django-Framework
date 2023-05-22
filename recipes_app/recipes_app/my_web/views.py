from django.shortcuts import render, redirect

from recipes_app.my_web.forms import RecipeCreateForm
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
    return render(request, 'edit.html')


def delete(request, pk):
    return render(request, 'delete.html')


def details(request, pk):
    return render(request, 'details.html')
