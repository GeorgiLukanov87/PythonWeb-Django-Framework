from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import views as auth_views


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


def register(request):
    return render(request, 'accounts/register-page.html')


def login(request):
    return render(request, 'accounts/login-page.html')


def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def to_github(request):
    return HttpResponseRedirect("https://github.com/GeorgiLukanov87/PythonWeb-Django-Framework/tree/main/petstagram")
