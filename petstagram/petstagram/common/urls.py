from django.urls import path

from petstagram.common.views import show_index

urlpatterns = (
    path('', show_index, name='show index'),

)
