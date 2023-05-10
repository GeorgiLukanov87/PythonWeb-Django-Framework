from django.shortcuts import render, redirect

from car_collection_app.web.forms import ProfileCreateForm, ProfileDeleteForm, CarCreateForm, ProfileEditForm, \
    CarEditForm, CarDeleteForm
from car_collection_app.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


# BASE VIEWS.
def show_index(request):
    profile = get_profile()
    if profile is None:
        return render(request,'core/index.html')

    cars = Car.objects.all()
    context = {
        'hide_navigation': True,
        'cars':cars,
    }

    return render(
        request,
        'core/index.html',
        context,
    )


def show_catalogue(request):
    all_cars = Car.objects.all()
    count = len(all_cars)

    context = {
        'all_cars': all_cars,
        'count': count,
        'hide_navigation':True,
    }
    return render(
        request,
        'core/catalogue.html',
        context,

    )


# PROFILE VIEWS.
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
        'profile/profile-create.html',
        context,
    )


def calculate_total_cars_price(_cars):
    total_sum = sum([float(car.price) for car in _cars])
    return total_sum


def details_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_price = calculate_total_cars_price(cars)

    context = {
        'profile': profile,
        'cars': cars,
        'total_price': total_price,
        'hide_navigation':True,
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
            return redirect('show index')

    context = {
        'form': form,
        'hide_navigation': True,
    }

    return render(
        request,
        'profile/profile-edit.html',
        context,
    )


def delete_profile(request):
    profile = get_profile()

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
        'hide_navigation':True,
    }

    return render(
        request,
        'profile/profile-delete.html',
        context,
    )


# CAR VIEWS.
def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'form': form,
        'hide_navigation':True,
               }
    return render(
        request,
        'car/car-create.html',
        context,
    )


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car,
        'hide_navigation': True,
    }
    return render(
        request,
        'car/car-details.html',
        context,
    )


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'car': car,
        'form': form,
    }

    return render(
        request,
        'car/car-edit.html',
        context,
    )


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'car': car,
        'form': form,
    }
    return render(
        request,
        'car/car-delete.html',
        context,
    )
