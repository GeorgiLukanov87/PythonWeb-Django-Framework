from django.shortcuts import render


def index(request):
    profile = None
    if profile:
        return render(request, 'common/home-with-profile.html')
    else:
        return render(request, 'common/home-no-profile.html')


def profile_details(request):
    return render(request, 'common/profile.html')


def add_note(request):
    return render(request, 'note/note-create.html')


def edit_note(request, pk):
    return render(request, 'note/note-edit.html')


def delete_note(request, pk):
    return render(request, 'note/note-delete.html')


def details_note(request, pk):
    return render(request, 'note/note-details.html')
