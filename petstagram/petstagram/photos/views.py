from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.forms import CommentForm
from petstagram.core.photo_utils import find_photo_by_pk
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm


# photos/views.py
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {
        'form': form,
    }

    return render(
        request,
        'photos/photo-add-page.html',
        context,
    )


def show_photo_details(request, pk):
    photo = find_photo_by_pk(pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
        'is_owner': request.user == photo.user,

    }

    return render(
        request,
        'photos/photo-details-page.html',
        context,
    )


def get_post_photo_form(request, form, success_url, template_path, pk=None):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, template_path, context)


def edit_photo(request, pk):
    photo = find_photo_by_pk(pk)
    return get_post_photo_form(
        request,
        PhotoEditForm(request.POST or None, instance=photo),
        success_url=reverse('show index'),
        template_path='photos/photo-edit-page.html',
        pk=pk,
    )


def delete_photo(request, pk):
    photo = find_photo_by_pk(pk)

    return get_post_photo_form(
        request,
        PhotoDeleteForm(request.POST or None, instance=photo),
        success_url=reverse('show index'),
        template_path='photos/photo-delete-page.html',
        pk=pk,
    )
