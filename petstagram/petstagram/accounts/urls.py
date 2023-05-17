from django.urls import path, include

from petstagram.accounts.views import register, login, show_profile_details, edit_profile, delete_profile

# accounts/urls.py

urlpatterns = (
    path('register/', register, name='register'),
    path('login/', login, name='login'),

    path('profile/<int:pk>/', include(
        [
            path('', show_profile_details, name='profile details'),
            path('edit/', edit_profile, name='profile edit'),
            path('delete/', delete_profile, name='profile delete'),
        ]
    )),

)
