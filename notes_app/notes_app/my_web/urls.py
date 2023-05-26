from django.urls import path, include

from notes_app.my_web.views import index, profile_details, \
    profile_delete, AddNoteCBV, DeleteNoteCBV, EditNoteCBV, DetailsNoteCBV

# http://localhost:8000/ - home page
# http://localhost:8000/add - add note page
# http://localhost:8000/edit/1 - edit note page
# http://localhost:8000/delete/1 - delete note page
# http://localhost:8000/details/1 - note details page
# http://localhost:8000/profile - profile page


urlpatterns = [
    path('', include([
        path('', index, name='index'),
        path('edit/<int:pk>/', EditNoteCBV.as_view(), name='edit-note'),
        path('delete/<int:pk>/', DeleteNoteCBV.as_view(), name='delete-note'),
        path('details/<int:pk>/', DetailsNoteCBV.as_view(), name='details-note'),

        path('add_note/', AddNoteCBV.as_view(), name='add-note'),

    ])),

    path('profile/', profile_details, name='profile-details'),
    path('profile/delete/', profile_delete, name='profile-delete'),

]
