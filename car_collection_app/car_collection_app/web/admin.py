from django.contrib import admin

from car_collection_app.web.models import Profile, Car


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class PlantAdmin(admin.ModelAdmin):
    pass
