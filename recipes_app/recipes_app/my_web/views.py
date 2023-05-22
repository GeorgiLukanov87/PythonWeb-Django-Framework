from django.shortcuts import render

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
    return render(request, 'create.html')


def edit(request, pk):
    return render(request, 'edit.html')


def delete(request, pk):
    return render(request, 'delete.html')


def details(request, pk):
    return render(request, 'details.html')
