from django.contrib import admin
from .models import Video, Frame
# Register your models here.

@admin.register(Video)
class Video(admin.ModelAdmin):
  list_display = (
    "id",
    "start_time",
    "end_time",
    "created_at",
  )
  search_fields = (
    "id",
  )

@admin.register(Frame)
class Video(admin.ModelAdmin):
  list_display = (
    "id",
    "start_time",
    "end_time",
    "created_at",
  )
  search_fields = (
    "id",
  )
