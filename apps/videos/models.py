from django.db import models
from apps.flax_id.django.fields import FlaxId
# Create your models here.

class Video(models.Model):
    id = FlaxId(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(default=0)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    video_path = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id

class Frame(models.Model):
    id = FlaxId(primary_key=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    image_data = models.BinaryField(null=True, blank=True)
    segment_data = models.BinaryField(null=True, blank=True)
    segment_path = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
