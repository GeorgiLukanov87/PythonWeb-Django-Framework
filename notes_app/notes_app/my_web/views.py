from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as view

from notes_app.my_web.forms import NoteEditForm, NoteCreateForm, ProfileCreateForm, NoteDeleteForm, ProfileDeleteForm
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

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'common/delete-profile.html',
        context,
    )


class DeleteNoteCBV(view.DeleteView):
    template_name = 'note/note-delete.html'
    model = Note
    fields = '__all__'

    success_url = '/'


class AddNoteCBV(view.CreateView):
    template_name = 'note/note-create.html'
    model = Note
    fields = '__all__'

    # static redirect
    # success_url = '/'

    # dynamic redirect
    def get_success_url(self):
        return reverse('details-note', kwargs={
            'pk': self.object.pk,
        })


class EditNoteCBV(view.UpdateView):
    model = Note
    fields = '__all__'
    template_name = 'note/note-edit.html'

    def get_success_url(self):
        return reverse('details-note', kwargs={
            'pk': self.object.pk,
        })


class DetailsNoteCBV(view.DeleteView):
    model = Note
    fields = '__all__'
    template_name = 'note/note-details.html'
