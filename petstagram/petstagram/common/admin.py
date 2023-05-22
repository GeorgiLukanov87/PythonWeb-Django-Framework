from django.contrib import admin

from petstagram.common.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
