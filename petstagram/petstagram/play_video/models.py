from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    VIDEO_TITLE_MAX_LEN = 100
    title = models.CharField(max_length=VIDEO_TITLE_MAX_LEN)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']
