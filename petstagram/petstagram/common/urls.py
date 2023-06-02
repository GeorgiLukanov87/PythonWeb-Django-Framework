from django.urls import path

from petstagram.common.views import show_index, like_functionality, add_comment, share, redirect_to_index

urlpatterns = (
    path('', show_index, name='show index'),
    path('redirect_to_index/', redirect_to_index, name='redirect_to_index'),

    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', share, name='share'),
    path('comment/<int:photo_id>/', add_comment, name='add comment'),
)
