from django.contrib import admin

from recipes_app.my_web.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
