
from django.urls import path, include

from my_plant_app.web.views import create_profile, show_index, details_profile, edit_profile, delete_profile, \
    show_catalogue, create_plant, details_plant, edit_plant, delete_plant

urlpatterns = (
    path('', show_index, name='show index'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),

    path('catalogue/', show_catalogue, name='show catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<pk>/', details_plant, name='details plant'),
    path('edit/<pk>/', edit_plant, name='edit plant'),
    path('delete/<pk>/', delete_plant, name='delete plant'),
)
