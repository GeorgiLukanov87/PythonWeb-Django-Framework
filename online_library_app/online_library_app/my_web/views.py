from django.shortcuts import render


# Create your views here.

def index(request):
    profile = True

    if profile:
        return render(request, 'common/home-with-profile.html')  # Dashboard
    else:
        return render(request, 'common/home-no-profile.html')


# book's views
def add_book(request):
    return render(request, 'book/add-book.html')


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
