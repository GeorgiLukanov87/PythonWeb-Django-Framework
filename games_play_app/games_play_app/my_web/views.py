from django.shortcuts import render, redirect

from games_play_app.my_web.forms import ProfileCreateForm, GameCreateForm, ProfileEditForm, ProfileDeleteForm, \
    GameEditForm, GameDeleteForm
from games_play_app.my_web.models import Profile, Game


def __calculate_average_rating(_all_games):
    average_rating = sum([float(game.rating) for game in _all_games])
    return average_rating


def get_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist as ex:
        return None


def show_index(request):
    games = Game.objects.all()
    profile = get_profile()
    context = {
        'hide_nav': True,
    }
    if profile is None:
        return render(
            request,
            'core/home-page.html',
            context,
        )

    context = {
        'games': games,
        'hide_nav': False,

    }
    return render(
        request,
        'core/home-page.html',
        context,
    )


def show_dashboard(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }
    return render(
        request,
        'core/dashboard.html',
        context,
    )


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')

    context = {
        'form': form,
        'hide_nav': True,
    }

    return render(
        request,
        'profile/create-profile.html',
        context,
    )


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    count = len(games)
    average_rating = 0.0
    if count:
        average_rating = __calculate_average_rating(games) / count

    context = {
        'profile': profile,
        'games': games,
        'count': count,
        'average_rating': average_rating,
    }

    return render(
        request,
        'profile/details-profile.html',
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
    }

    return render(
        request,
        'profile/delete-profile.html',
        context,
    )


def create_game(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')

    context = {
        'form': form,
        'hide_nav': False,
    }

    return render(
        request,
        'game/create-game.html',
        context,
    )


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'game': game,
    }

    return render(
        request,
        'game/details-game.html',
        context,
    )


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')

    context = {
        'form': form,
        'game': game,
    }

    return render(
        request,
        'game/edit-game.html',
        context,
    )


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')

    context = {
        'form': form,
        'game': game,
    }

    return render(
        request,
        'game/delete-game.html',
        context,
    )
