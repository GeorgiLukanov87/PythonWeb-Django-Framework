# http://localhost:8000/ - home page

# http://localhost:8000/add/ - add book page
# http://localhost:8000/edit/1 - edit book page
# http://localhost:8000/details/1 - book details page

# http://localhost:8000/profile/ - profile page
# http://localhost:8000/profile/edit/ - edit profile page
# http://localhost:8000/profile/delete/ - delete profile page
from django.urls import path, include

from online_library_app.my_web.views import index, add_book, edit_book, details_book, profile_page, edit_profile, \
    delete_profile, create_profile

urlpatterns = (
    path('', index, name='index'),

    path('add/', add_book, name='add-book'),
    path('edit/<int:pk>/', edit_book, name='edit-book'),
    path('details/<int:pk>/', details_book, name='details-book'),

    path('profile/', include([
        path('', profile_page, name='profile-page'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete-profile'),
        path('create/', create_profile, name='create-profile'),
    ]))
)
