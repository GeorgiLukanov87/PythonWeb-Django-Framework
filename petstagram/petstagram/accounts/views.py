from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic

from petstagram.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SingInView(generic.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('show index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('show index')


# ----------------------------------------------
def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def to_github(request):
    return HttpResponseRedirect(
        "https://github.com/GeorgiLukanov87/PythonWeb-Django-Framework/tree/main/petstagram"
    )
