from django.urls import path

from xxxx.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
