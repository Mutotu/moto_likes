from django.contrib import admin

# Register your models here.

from .models import Profile, Photo, Interaction

admin.site.register(Profile)
admin.site.register(Photo)
admin.site.register(Interaction)