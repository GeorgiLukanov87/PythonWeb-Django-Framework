from django.shortcuts import render, redirect

from online_library_app.my_web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, BookCreateForm, \
    BookEditForm, BookDeleteForm
from online_library_app.my_web.models import Profile, Book


def index(request):
    profile = Profile.objects.first()
    books = Book.objects.all()

    if profile is None:
        return redirect("create-profile")

    context = {
        'profile': profile,
        'books': books,
    }

    return render(
        request,
        'common/home-with-profile.html',
        context,
    )


def create_profile(request):
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


# profile's views
def profile_page(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }

    return render(
        request,
        'profile/profile.html',
        context,
    )


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(
        request,
        'profile/edit-profile.html',
        context,
    )


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(
        request,
        'profile/delete-profile.html',
        context,
    )


# book's views
def add_book(request):
    if request.method == 'GET':
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'book/add-book.html',
        context,
    )


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            # return redirect(f'/details/{book.pk}') -> redirect to the same book (edited)
            return redirect('index')

    context = {
        'form': form,
        'book': book,
    }

    return render(
        request,
        'book/edit-book.html',
        context,
    )


def details_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    context = {
        'book': book,
    }

    return render(
        request,
        'book/book-details.html',
        context,
    )


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = BookDeleteForm(instance=book)
    else:
        form = BookDeleteForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'book': book,
        'form': form,
    }

    return render(
        request,
        'book/delete-book.html',
        context,
    )
