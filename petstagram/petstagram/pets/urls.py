from django.urls import path, include

from petstagram.pets.views import add_pet, show_pet_details, edit_pet, delete_pet

# pets/urls
# http://127.0.0.1:8000/pets/goto/pet/Buddy/ + edit/delete

urlpatterns = (
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include(
        [
            path('', show_pet_details, name='show pet details'),
            path('edit/', edit_pet, name='edit pet'),
            path('delete/', delete_pet, name='delete pet'),
        ]
    )),
)
