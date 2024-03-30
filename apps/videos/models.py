from django.db import models
from apps.flax_id.django.fields import FlaxId
# Create your models here.
from django.utils.translation import gettext_lazy as _
import os

class CameraStatus(models.TextChoices):
    ACTIVE = 'active', _('Active')
    INACTIVE = 'inactive', _('Inactive')

class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255, choices=CameraStatus.choices, default=CameraStatus.ACTIVE)
    model_type = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VideoSegment(models.Model):
    id = FlaxId(primary_key=True)
    camera = models.ForeignKey('Camera', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    video_file = models.FileField(upload_to='public/videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def delete(self, *args, **kwargs):
        if self.video_file:
            if os.path.isfile(self.video_file.path):
                os.remove(self.video_file.path)
        super().delete(*args, **kwargs)
