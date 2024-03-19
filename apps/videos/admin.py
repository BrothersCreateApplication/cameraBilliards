from django.contrib import admin
from .models import Camera, VideoSegment
from django.utils.html import format_html
# Register your models here.

@admin.register(Camera)
class Camera(admin.ModelAdmin):
  list_display = (
    "id",
    "name",
    "ip_address",
    "username",
    "created_at",
  )
  search_fields = (
    "id",
  )

@admin.register(VideoSegment)
class VideoSegment(admin.ModelAdmin):
  list_display = (
    "id",
    "start_time",
    "end_time",
    "created_at",
  )
  search_fields = (
    "id",
  )

