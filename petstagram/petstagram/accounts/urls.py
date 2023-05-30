from django.urls import path, include

from petstagram.accounts.views import show_profile_details, edit_profile, delete_profile, to_github, SignInView, \
    SingInView

# accounts/urls.py

urlpatterns = (
    path('register/', SingInView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('to_github/', to_github, name='out'),

    path('profile/<int:pk>/', include(
        [
            path('', show_profile_details, name='profile details'),
            path('edit/', edit_profile, name='profile edit'),
            path('delete/', delete_profile, name='profile delete'),
        ]
    )),

)
