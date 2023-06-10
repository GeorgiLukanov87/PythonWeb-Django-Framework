from django.contrib import admin
from django.urls import path, include

from xxxx.web.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('xxxx.web.urls'))

]
