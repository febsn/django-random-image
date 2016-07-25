from django.contrib import admin

from .models import ImageContainer

@admin.register(ImageContainer)
class ImageContainerAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'image',)
