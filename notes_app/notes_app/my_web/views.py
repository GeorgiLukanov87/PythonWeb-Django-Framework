from django.shortcuts import render

from notes_app.my_web.models import Profile, Note


def index(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    if profile:

        context = {
            'profile': profile,
            'notes': notes,
        }

        return render(
            request,
            'common/home-with-profile.html',
            context,
        )

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
