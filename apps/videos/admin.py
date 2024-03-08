from django.contrib import admin
from .models import Video, Frame
from django.utils.html import format_html
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
class Frame(admin.ModelAdmin):
  list_display = (
    "id",
    "preview_image",
    "start_time",
    "end_time",
    "created_at",
  )
  search_fields = (
    "id",
  )
  readonly_fields = ('preview_image',)

  def preview_image(self, obj):
      return format_html('<img src="data:image/jpeg;base64,{}" style="max-width:200px;max-height:200px;">',
                           obj.image_data)
  preview_image.short_description = 'Image Preview'
