from django.contrib import admin

from games_play_app.my_web.models import Profile, Game


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
