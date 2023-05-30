from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetEditForm, PetCreateForm, PetDeleteForm
from petstagram.pets.models import Pet


@login_required
# pets/views.py
def add_pet(request):
    if request.method == "GET":
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile details', pk=request.user.pk)

    context = {
        'form': form,

    }

    return render(
        request,
        'pets/pet-add-page.html',
        context,
    )


def show_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'username': username,
        'pet_slug': pet_slug,
    }

    return render(
        request,
        'pets/pet-details-page.html',
        context,
    )


# http://127.0.0.1:8000/pets/goto/pet/pesho-5/
def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('show pet details', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'pet': pet,
        'username': username,
        'pet_slug': pet_slug,
    }
    return render(
        request,
        'pets/pet-edit-page.html',
        context,
    )


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)

    context = {
        'form': form,
        'pet': pet,
        'pet_slug': pet_slug,
        'username': username,
    }

    return render(
        request,
        'pets/pet-delete-page.html',
        context,
    )
