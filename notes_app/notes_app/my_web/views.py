from django.shortcuts import render, redirect

from notes_app.my_web.forms import NoteEditForm, NoteCreateForm, ProfileCreateForm, NoteDeleteForm
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
        if request.method == 'GET':
            form = ProfileCreateForm()
        else:
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

        context = {
            'form': form,
        }
        return render(
            request,
            'common/home-no-profile.html',
            context,
        )


def profile_details(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(
        request,
        'common/profile.html',
        context,
    )


def profile_delete(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    notes.delete()
    profile.delete()
    return redirect('index')


def add_note(request):
    if request.method == 'GET':
        form = NoteCreateForm()
    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'note/note-create.html',
        context,
    )


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'GET':
        form = NoteEditForm(instance=note)
    else:
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
    }

    return render(
        request,
        'note/note-edit.html',
        context,

    )


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)
    else:
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
    }

    return render(
        request,
        'note/note-delete.html',
        context,
    )


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }

    return render(
        request,
        'note/note-details.html',
        context,

    )
