from django.shortcuts import render


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def show_pet_details(request, username, pet, pet_name):
    return render(request, 'pets/pet-details-page.html')


def edit_pet(request, username, pet, pet_name):
    return render(request, 'pets/pet-edit-page.html')


def delete_pet(request, username, pet, pet_name):
    return render(request, 'pets/pet-delete-page.html')
