import pyperclip
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


# common/views.py
def show_index(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(
        request,
        'common/home-page.html',
        context,
    )


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id, user_id=request.user.pk)

    if liked_object:
        liked_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


def share(request, photo_id):
    photo_details_url = reverse('show photo details', kwargs={
        'pk': photo_id
    })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


@login_required
def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.filter(pk=photo_id).get()

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(
            request.META['HTTP_REFERER'] + f'#{photo_id}'
        )


@login_required
def redirect_to_index(request):
    return redirect('show index')
