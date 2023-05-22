from django.urls import path

from recipes_app.my_web.views import index, create, edit, delete, details

urlpatterns = (
    path('', index, name='index'),
    path('create/', create, name='create'),

    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('details/<int:id>/', details, name='details'),
)
