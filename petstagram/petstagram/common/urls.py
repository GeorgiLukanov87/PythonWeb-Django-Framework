from django.urls import path

from petstagram.common.views import show_index, like_functionality, copy_link_to_clipboard, add_comment

urlpatterns = (
    path('', show_index, name='show index'),

    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>/', add_comment, name='add comment'),

)
