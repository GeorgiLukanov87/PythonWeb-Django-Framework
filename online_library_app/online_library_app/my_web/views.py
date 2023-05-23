from django.shortcuts import render, redirect

from online_library_app.my_web.forms import ProfileCreateForm
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


# book's views
def add_book(request):

    return render(
        request,
        'book/add-book.html',

    )


def edit_book(request, pk):
    return render(request, 'book/edit-book.html')


def details_book(request, pk):
    return render(request, 'book/book-details.html')


# profile's views
def profile_page(request):
    return render(request, 'profile/profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')
