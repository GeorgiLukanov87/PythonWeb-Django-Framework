from django.shortcuts import render, redirect

from my_plant_app.web.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, ProfileEditForm, PlantDeleteForm, \
    ProfileDeleteForm
from my_plant_app.web.models import Profile, Plant


# Get profile function.
def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def show_index(request):
    profile = get_profile()
    if profile is None:
        return render(request, 'core/home-page.html')

    context = {
        'plant': Plant.objects.all(),
        'hide_nav_links': True,
    }

    return render(
        request,
        'core/home-page.html',
        context,

    )


# Show catalogue
def show_catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants,
        'hide_nav_links': True,

    }

    return render(
        request,
        'core/catalogue.html'
        , context,
    )


# Profile
def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'form': form,
    }

    return render(
        request,
        'profile/create-profile.html',
        context,
    )


def details_profile(request):
    profile = get_profile()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
        'hide_nav_links': True,

    }

    return render(
        request,
        'profile/profile-details.html',
        context,
    )


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }

    return render(
        request,
        'profile/edit-profile.html',
        context,
    )


def delete_profile(request):
    profile = Profile.objects.get()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(
        request,
        'profile/delete-profile.html',
        context,
    )


# Plants
def create_plant(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'form': form,
        'hide_nav_links': True,

    }
    return render(
        request,
        'plant/create-plant.html',
        context,
    )


def details_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant,
    }

    return render(
        request,
        'plant/plant-details.html',
        context,
    )


def edit_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'plant': plant,
        'form': form,
    }

    return render(
        request,
        'plant/edit-plant.html',
        context,
    )


def delete_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        form.is_valid()
        form.save()
        return redirect('show catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(
        request,
        'plant/delete-plant.html',
        context,
    )
