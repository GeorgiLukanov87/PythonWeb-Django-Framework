from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from petstagram.play_video.models import Video


@admin.register(Video)
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
