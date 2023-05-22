from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def create(request):
    return render(request, 'create.html')


def edit(request, pk):
    return render(request, 'edit.html')


def delete(request, pk):
    return render(request, 'delete.html')


def details(request, pk):
    return render(request, 'details.html')
